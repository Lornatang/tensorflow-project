"""
# author: shiyipaisizuo
# contact: shiyipaisizuo@gmail.com
# file: load_data.py
# time: 2018/7/25 23:08
# license: MIT
"""
import os
import random
import sys
import cv2

import dlib


dir_path = sys.argv[1]
numbers = sys.argv[2]

width, height = 64, 64  # Photo size 128 * 128.

# We used dlib's own frontal_face_detector as our feature extractor
detector = dlib.get_frontal_face_detector()
# Open camera parameters for input stream, can be camera or video file
camera = cv2.VideoCapture(0)


def exist(path):
    """If it exists, it is deleted, and no creation exists.

    Args:
        path: dir path
    """
    try:
        if os.path.exists(path):
            print(f"Dir ./{path} is exist!")
            print(f"Please remove dir ./{path}")
            return False
        else:
            os.makedirs(path)
            return True
    except OSError:
        print("Status 1! ERROR!")


def dispose_img(x, light=1, bias=0):
    """Change the brightness and contrast of the image.
    Args:
        x: input img
        light: light
        bias: bias

    Returns:
        x: output img
    """
    w = x.shape[1]
    h = x.shape[0]
    for i in range(0, w):
        for j in range(0, h):
            for c in range(3):
                tmp = int(x[j, i, c] * light + bias)
                if tmp > 255:
                    tmp = 255
                elif tmp < 0:
                    tmp = 0
                x[j, i, c] = tmp
    return x


def get_data_for_usb(path, n):
    """Get face data.

    Args:
        path: dir path
        n: numbers
    """
    for index in range(1, n + 1):
        print(f"Saved {index}.jpg to {path}/{index}.jpg")
        # Read photos from the camera.
        _, img = camera.read()
        # Turn it into a grayscale image.
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Face detection using detector.
        dets = detector(gray_img, 1)

        for i, d in enumerate(dets):
            x1 = d.top() if d.top() > 0 else 0
            y1 = d.bottom() if d.bottom() > 0 else 0
            x2 = d.left() if d.left() > 0 else 0
            y2 = d.right() if d.right() > 0 else 0

            face = img[x1:y1, x2:y2]
            # Randomly adjust the contrast and brightness of the image.
            face = dispose_img(face, random.uniform(0.5, 1.5), random.randint(-50, 50))
            # Convert the image to the specified size.
            face = cv2.resize(face, (width, height))

            cv2.imwrite(path + '/' + str(index) + '.jpg', face)


def get_data_for_img():
    pass


if __name__ == "__main__":
    if exist(dir_path):
        get_data_for_usb(dir_path, numbers)
    else:
        print("Status 1! ERROR!")
