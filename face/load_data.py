"""
# author: shiyipaisizuo
# contact: shiyipaisizuo@gmail.com
# file: load_data2.py
# time: 2018/7/27 02:10
# license: MIT
"""
import os
import sys

import cv2
import dlib

img_path = './data/' + sys.argv[1]
width, height = 128, 128

if not os.path.exists(img_path):
    os.makedirs(img_path)


# 使用dlib自带的frontal_face_detector作为我们的特征提取器
detector = dlib.get_frontal_face_detector()
# 打开摄像头 参数为输入流，可以为摄像头或视频文件
camera = cv2.VideoCapture(0)

index = 1
while True:
    if index <= 100:
        os.system("clear")
        print(f"{'#' * (index // 2):50s} " + f"{index}%")
        print(f"Save to {img_path}/{index}.jpg")
        # 从摄像头读取照片
        success, img = camera.read()
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

            cv2.imwrite(f"{img_path}/{str(sys.argv[1]) + str(index)}.jpg", face)

            index += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('Finished!')
        break
