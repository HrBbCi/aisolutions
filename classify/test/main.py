import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import matplotlib.pyplot as plt
import operator
import cv2
import numpy as np

train_dir = "data/train"
validation_dir = "data/test"

def get_images(object_category, data_directory):
    if (not os.path.exists(data_directory)):
        print("Data not found!")
        return
    obj_category_dir = os.path.join(os.path.join(data_directory,"train"),object_category)
    images = [os.path.join(obj_category_dir,img) for img in os.listdir(obj_category_dir)]
    return images

def read_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # correct colors
    img = cv2.resize(img, (300,200), interpolation=cv2.INTER_CUBIC)
    return img

class_names = ['car', 'cup', 'chair']
i = 0
X = np.ndarray((10000, 200, 300, 3), dtype=np.uint8)
Y = []
data_directory = "data"
categories = os.listdir(data_directory + "/train/")
object_images_count_dict = {}
for category in categories:
    object_images_count_dict[category] = len(os.listdir(data_directory+"/train/"+category))
object_images_count_dict = sorted(object_images_count_dict.items(), key=operator.itemgetter(1), reverse=True)
print(object_images_count_dict)

for category,_ in object_images_count_dict:
    if category in class_names:
      for image in get_images(category, data_directory):
          if not image.endswith('.jpg'):
              continue
          X[i] = read_image(image)
          Y.insert(i,category) 
          i += 1
      print(str(i+1) + "  " + category)