# import the necessary packages
from src.model import SiameseModel, get_embedding_module
from matplotlib import pyplot as plt
from src import config
from sklearn.metrics import confusion_matrix
from tensorflow import keras
import tensorflow as tf
import numpy as np
import os


# define function to compute metrics
def metrics(predictions, label_gt):
    TP_binary = np.logical_and(predictions, label_gt)
    FP_binary = np.logical_and(predictions, np.logical_not(label_gt))
    TN_binary = np.logical_and(np.logical_not(predictions), np.logical_not(label_gt))
    FN_binary = np.logical_and(np.logical_not(predictions), label_gt)
    
    TP = sum(TP_binary )
    FP = sum(FP_binary )
    TN = sum(TN_binary )
    FN = sum(FN_binary )
    precision = TP/(TP+FP)
    recall = TP/(FN+TP)
    F1 = (2*precision*recall)/(precision+recall)
    
    return precision, recall, F1

modelPath = config.MODEL_PATH
### Loading pre-trained siamese model for inference
print(f"[INFO] loading the siamese network from {modelPath}...")
siameseNetwork = keras.models.load_model(filepath=modelPath)
siameseModel = SiameseModel(
	siameseNetwork=siameseNetwork,
	margin=0.5,
	lossTracker=keras.metrics.Mean(name="loss"),
)

DatabasePath = 'data'
img_height, img_width = config.IMAGE_SIZE
print(f"[INFO] Setting-up Data Pipeline...")
test_ds = tf.keras.utils.image_dataset_from_directory(
  config.TEST_DATASET,
  seed=123,
  image_size=(img_height, img_width),
  batch_size=1)

print(f"[INFO] Making Predictions on Test Set...")
test_images = []
test_labels = []

# Collect all images and labels first
for sample, label in test_ds:
    test_images.append(sample)
    test_labels.append(label.numpy()[0])

test_images = np.concatenate(test_images, axis=0)
test_labels = np.array(test_labels)

embedding_network = get_embedding_module(config.IMAGE_SIZE)

# Precompute all embeddings
test_images_norm = test_images / 255.0
all_embeddings = []
for img in test_images_norm:
  embedding = embedding_network(np.expand_dims(img, axis=0))
  all_embeddings.append(embedding.numpy()[0])
all_embeddings = np.array(all_embeddings)

predictions = []
ground_truth = []
for i, (anchor_embedding, anchor_label) in enumerate(zip(all_embeddings, test_labels)):
  distances = []
  candidate_labels = []
  for j, (candidate_embedding, candidate_label) in enumerate(zip(all_embeddings, test_labels)):
    if i == j:
      continue  # skip self-comparison

    distance = np.sum(np.square(anchor_embedding - candidate_embedding))
    distances.append(distance)
    candidate_labels.append(candidate_label)

  # Find nearest neighbor
  if distances:
      # min_idx refers to the nearest neighbor index
      min_idx = np.argmin(distances)
      predictions.append(candidate_labels[min_idx])
      ground_truth.append(anchor_label)

ground_truth = np.asarray(ground_truth)
predictions = np.asarray(predictions)

print(f"[INFO] Evaluating the model...")
##Computing Metrics
N = ground_truth.shape[0]
accuracy = (ground_truth == predictions).sum() / N

# calculating the confusion matrix
cm = confusion_matrix(ground_truth, predictions)
recall = np.diag(cm) / np.sum(cm, axis = 1)
precision = np.diag(cm) / np.sum(cm, axis = 0)
recallOverall = np.mean(recall)
precisionOverall = np.mean(precision)
F1_overall = 2*recallOverall*precisionOverall/(recallOverall+precisionOverall)

print(f"[INFO] Accuracy: {accuracy:.4f}")
print(f"[INFO] Overall Precision: {precisionOverall:.4f}")
print(f"[INFO] Overall Recall: {recallOverall:.4f}")
print(f"[INFO] Overall F1 Score: {F1_overall:.4f}")
print(f"[INFO] Confusion Matrix:\n{cm}")
