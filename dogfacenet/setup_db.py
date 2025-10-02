import chromadb
import os
import tensorflow as tf
import tensorflow.keras.backend as K
from dogfacenet import triplet, triplet_acc
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input


chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="teste")

# Load the trained model
model = tf.keras.models.load_model('../output/model/2025.08.19/2025.08.19.dogfacenet.0.h5', custom_objects={'triplet':triplet,'triplet_acc':triplet_acc})

# Custom dataset class for test images
class TestDataset:
    def __init__(self, test_dir):
        self.test_dir = test_dir
        self.images = []
        self.labels = []
        
        for class_name in os.listdir(test_dir):
            class_path = os.path.join(test_dir, class_name)
            if os.path.isdir(class_path):
                for img_name in os.listdir(class_path):
                    self.images.append(os.path.join(class_path, img_name))
                    self.labels.append(class_name)
    
    def __len__(self):
        return len(self.images)
    
    def load_and_preprocess_image(self, img_path):
        image = load_img(img_path, target_size=(224, 224))
        image = img_to_array(image)
        image = preprocess_input(image)
        return image

# Load test dataset
test_dataset = TestDataset('../data/test')

print(test_dataset.images)

# Extract embeddings and add to ChromaDB
embeddings = []
metadatas = []
ids = []

batch_size = 32
for i in range(0, len(test_dataset), batch_size):
    batch_images = []
    batch_labels = []
    batch_paths = []
    
    # Prepare batch
    for j in range(i, min(i + batch_size, len(test_dataset))):
        img_path = test_dataset.images[j]
        label = test_dataset.labels[j]
        image = test_dataset.load_and_preprocess_image(img_path)
        
        batch_images.append(image)
        batch_labels.append(label)
        batch_paths.append(img_path)
    
    # Convert to numpy array and get embeddings
    batch_images = np.array(batch_images)
    batch_embeddings = model.predict(batch_images, verbose=0)
    
    # Add to collections
    for j, (embedding, label, path) in enumerate(zip(batch_embeddings, batch_labels, batch_paths)):
        embeddings.append(embedding.tolist())
        metadatas.append({"label": label, "image_path": path})
        ids.append(f"img_{i//batch_size}_{j}")

# Add embeddings to ChromaDB collection
collection.add(
    embeddings=embeddings,
    metadatas=metadatas,
    ids=ids
)

print(f"Added {len(embeddings)} embeddings to ChromaDB collection")