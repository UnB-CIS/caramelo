import tensorflow as tf
import os

# path to training and testing data
TRAIN_DATASET = "../data/train"
TEST_DATASET = "../data/test"

# model input image size
IMAGE_SIZE = (224, 224)

# batch size and the buffer size
BATCH_SIZE = 256
BUFFER_SIZE = BATCH_SIZE * 2    # determines the number of elements from which the next 
                                # element for the shuffled dataset is randomly drawn

# define autotune
AUTO = tf.data.AUTOTUNE

# define the training parameters
LEARNING_RATE = 0.0001
STEPS_PER_EPOCH = 50
VALIDATION_STEPS = 10
EPOCHS = 10

# define the path to save the model
OUTPUT_PATH = "models"
MODEL_PATH = os.path.join(OUTPUT_PATH, "siamese_network.keras")
# OUTPUT_IMAGE_PATH = os.path.join(OUTPUT_PATH, "output_image.png")