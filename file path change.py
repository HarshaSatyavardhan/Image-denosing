#128*128
#tif to jpeg
import os
import cv2

path = '/content/chasedb1/'
data = '/content/data/'

for filename in os.listdir(path):
  img = cv2.imread(path+filename)
  outfile = filename.split('.')[0]+'.jpg'
  cv2.imwrite(data+outfile,img,[int(cv2.IMWRITE_JPEG_QUALITY), 200])