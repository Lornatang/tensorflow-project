"""
# author: shiyipaisizuo
# contact: shiyipaisizuo@gmail.com
# file: load_data.py
# time: 2018/7/27 17:17
# license: MIT
"""
import os
import sys

import cv2
import dlib
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.DEBUG)

# 第一个参数代表图片目录，第二个参数代表模型保存位置
img_path = './data/' + sys.argv[1]
unknown_path = './data/'

model_path = '../../model/tensorflow/face_recognition/' + sys.argv[1] + '/model.ckpt'

width, height = 128, 128

if not os.path.exists(img_path):
    os.makedirs(img_path)

# 使用dlib自带的frontal_face_detector作为我们的特征提取器
detector = dlib.get_frontal_face_detector()
camera = cv2.VideoCapture(0)  # 打开相机


def load_data():
    index = 1
    while True:
        if index <= 100:
            os.system("clear")
            print(f"{'#' * (index // 10):10s} " + f"{index}%")
            print(f"Save to {img_path}/{index}.jpg")
            # 从摄像头读取照片
            _, img = camera.read()
            # 转为灰度图片
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 使用detector进行人脸检测
            dets = detector(gray_img, 1)

            for i, d in enumerate(dets):
                x1 = d.top() if d.top() > 0 else 0
                y1 = d.bottom() if d.bottom() > 0 else 0
                x2 = d.left() if d.left() > 0 else 0
                y2 = d.right() if d.right() > 0 else 0

                face = img[x1:y1, x2:y2]
                # 调整图片大小
                face = cv2.resize(face, (width, height))
                cv2.imshow('Camera', face)

                cv2.imwrite(f"{img_path}/{str(sys.argv[1]) + str(index)}.jpg", face)

                index += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print('Finished!')
            break


if __name__ == '__main__':
    load_data()
