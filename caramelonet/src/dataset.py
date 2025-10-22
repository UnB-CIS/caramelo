import tensorflow as tf
import numpy as np
import random
import os


class MapFunction():
	def __init__(self, imageSize):
		self.imageSize = imageSize

	def decode_and_resize(self, imagePath):
		image = tf.io.read_file(imagePath)
		image = tf.image.decode_jpeg(image, channels=3)
		
		# convert the image data type from uint8 to float32 and then resize
		# the image to the set image size
		image = tf.image.convert_image_dtype(image, dtype=tf.float32)
		image = tf.image.resize(image, self.imageSize)
		
		return image
	
	def __call__(self, anchor, positive, negative):
		anchor = self.decode_and_resize(anchor)
		positive = self.decode_and_resize(positive)
		negative = self.decode_and_resize(negative)
		
		return (anchor, positive, negative)
	
class TripletGenerator:
	def __init__(self, datasetPath):
		# create an empty list which will contain the subdirectory
		# names of the `dataset` directory with more than one image
		# in it
		self.classesNames = list()
		
		for folderName in os.listdir(datasetPath):
			# build the subdirectory name
			absoluteFolderName = os.path.join(datasetPath, folderName)
			numImages = len(os.listdir(absoluteFolderName))
			if numImages > 1:
				self.classesNames.append(absoluteFolderName)
		
		# create a dictionary of classes names to their image names
		self.allClasses = self.generate_all_classes_dict()
	
	def generate_all_classes_dict(self):
		# create an empty dictionary that will be populated with
		# directory names as keys and image names as values
		allClasses = dict()
		
		for className in self.classesNames:
			imageNames = os.listdir(className)
			classPhotos = [
				os.path.join(className, imageName) for imageName in imageNames
			]
			allClasses[className] = classPhotos
		
		return allClasses
	
	def get_next_element(self):
		# create an infinite generator
		while True:
			# draw the anchor and positive sample at random
			anchorName = random.choice(self.classesNames)
			temporaryNames = self.classesNames.copy()
			temporaryNames.remove(anchorName)
			
			# draw a negative sample at random from the list of people
			# without the anchor
			negativeName = random.choice(temporaryNames)
			
			# draw two images from the anchor folder without replacement
			(anchorPhoto, positivePhoto) = np.random.choice(
				a=self.allClasses[anchorName],
				size=2,
				replace=False
			)
			
			# draw an image from the negative folder
			negativePhoto = random.choice(self.allClasses[negativeName])
			
			yield (anchorPhoto, positivePhoto, negativePhoto)