import os
import random
import sys

import cv2
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

import dlib

dir_path = input("Please input you want to save the address of the file.\n>>> ")
obama_path = './obama/'
width, height = 128, 128

imgs = []
labs = []

# 使用dlib自带的frontal_face_detector作为我们的特征提取器
detector = dlib.get_frontal_face_detector()

camera = cv2.VideoCapture(0)


def get_padding_size(x):
    """

    Args:
        x:

    Returns:

    """
    h, w, _ = x.shape
    top, bottom, left, right = (0, 0, 0, 0)
    longest = max(h, w)

    if w < longest:
        tmp = longest - w
        # //表示整除符号
        left = tmp // 2
        right = tmp - left
    elif h < longest:
        tmp = longest - h
        top = tmp // 2
        bottom = tmp - top
    else:
        pass
    return top, bottom, left, right


def read_data(path, h=width, w=height):
    for filename in os.listdir(path):
        if filename.endswith('.jpg'):
            filename = path + '/' + filename

            img = cv2.imread(filename)

            top, bottom, left, right = get_padding_size(img)
            # 将图片放大， 扩充图片边缘部分
            img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            img = cv2.resize(img, (h, w))

            imgs.append(img)
            labs.append(path)


read_data(dir_path)
read_data(obama_path)
# 将图片数据与标签转换成数组
imgs = np.array(imgs)
labs = np.array([[0, 1] if lab == dir_path else [1, 0] for lab in labs])
# 随机划分测试集与训练集
train_x, test_x, train_y, test_y = train_test_split(imgs, labs, test_size=0.05, random_state=random.randint(0, 100))
# 参数：图片数据的总数，图片的高、宽、通道
train_x = train_x.reshape(train_x.shape[0], width, height, 3)
test_x = test_x.reshape(test_x.shape[0], width, height, 3)
# 将数据转换成小于1的数
train_x = train_x.astype('float32') / 255.0
test_x = test_x.astype('float32') / 255.0

print('train size:%s, test size:%s' % (len(train_x), len(test_x)))
# 图片块，每次取128张图片
batch_size = 2
num_batch = len(train_x) / batch_size

X = tf.placeholder(tf.float32, [None, width, height, 3])
y = tf.placeholder(tf.float32, [None, 2])

keep_prob = tf.placeholder(tf.float32)


def weight(shape):
    init = tf.random_normal(shape, stddev=0.01)
    return tf.Variable(init)


def bias(shape):
    init = tf.random_normal(shape)
    return tf.Variable(init)


def conv2d(input_, w):
    return tf.nn.conv2d(input_, w, strides=[1, 1, 1, 1], padding='SAME')


def max_pool(input_):
    return tf.nn.max_pool(input_, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def cnn():
    # 第一层
    w1 = weight([3, 3, 3, 32])  # 卷积核大小(3,3)， 输入通道(3)， 输出通道(32)
    b1 = bias([32])
    # 卷积
    conv1 = tf.nn.relu(conv2d(X, w1) + b1)
    # 池化
    pool1 = max_pool(conv1)
    # 减少过拟合，随机让某些权重不更新
    drop1 = tf.nn.dropout(pool1, keep_prob=0.5)

    # 第二层
    w2 = weight([3, 3, 32, 64])
    b2 = bias([64])
    conv2 = tf.nn.relu(conv2d(drop1, w2) + b2)
    pool2 = max_pool(conv2)
    drop2 = tf.nn.dropout(pool2, keep_prob=0.5)

    # 第三层
    w3 = weight([3, 3, 64, 128])
    b3 = bias([128])
    conv3 = tf.nn.relu(conv2d(drop2, w3) + b3)
    pool3 = max_pool(conv3)
    drop3 = tf.nn.dropout(pool3, keep_prob=0.5)

    # 全连接层
    wf = weight([8 * 8 * 128, 512])
    bf = bias([512])
    drop3_flat = tf.reshape(drop3, [-1, 8 * 8 * 128])
    dense = tf.nn.relu(tf.matmul(drop3_flat, wf) + bf)
    drop = tf.nn.dropout(dense, keep_prob=0.75)

    # 输出层
    wc = weight([512, 1])
    bc = bias([2])
    out = tf.add(tf.matmul(drop, wc), bc)

    return out


pred = cnn()
predict = tf.argmax(pred, 1)

saver = tf.train.Saver()
sess = tf.Session()
saver.restore(sess, './model/model.ckpt')


def is_my_face(image):
    res = sess.run(predict, feed_dict={X: [image / 255.0], keep_prob: 1.0})
    if res[0] == 1:
        return True
    else:
        return False


def main():
    _, img = camera.read()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray_image, 1)

    for i, d in enumerate(dets):
        x1 = d.top() if d.top() > 0 else 0
        y1 = d.bottom() if d.bottom() > 0 else 0
        x2 = d.left() if d.left() > 0 else 0
        y2 = d.right() if d.right() > 0 else 0
        face = img[x1:y1, x2:y2]
        # 调整图片的尺寸
        face = cv2.resize(face, (width, height))
        print(f"Is this my face? {is_my_face(face)}")

        cv2.rectangle(img, (x2, x1), (y2, y1), (255, 0, 0), 3)
        cv2.imshow('image', img)
        key = cv2.waitKey(30) & 0xff
        if key == 27:
            sys.exit(0)


if __name__ == '__main__':
    while True:
        main()
