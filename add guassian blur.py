#

import cv2
import numpy as np
import skimage
import os

#load images from a folder

def load_images_folder(folder):
  images = []
  for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))

    noise_img = skimage.util.random_noise(img, mode='gaussian', var=0.01)
    noise_img = (255*noise_img).astype(np.uint8)
    cv2.imwrite(filename, noise_img)
  


load_images_folder('/content/data')

