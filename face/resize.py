import os

import cv2


def resize(path_dir):
  for files in os.listdir(path_dir):
    file = os.path.join(path_dir, files)
    img = cv2.imread(file)
    img = cv2.resize(img, (256, 256))
    cv2.imwrite(img)


resize('./train/')
resize('./val/')