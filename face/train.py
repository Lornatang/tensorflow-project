"""
# author: shiyipaisizuo
# contact: shiyipaisizuo@gmail.com
# file: trains.py
# time: 2018/7/27 17:12
# license: MIT
"""
import os
import sys

import cv2
import dlib
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

tf.logging.set_verbosity(tf.logging.DEBUG)

# 第一个参数代表图片目录，第二个参数代表模型保存位置
img_path = './data/' + sys.argv[1]
unknown_path = './data/'

model_path = '../../model/tensorflow/face_recognition/' + sys.argv[1] + '/model.ckpt'

width, height = 128, 128

LEARNING_RATE = 1e-3
MAX_EPOCH = int(sys.argv[2])
BATCH_SIZE = 64
DISPLAY_EPOCH = MAX_EPOCH // 5


imgs = []
labs = []

if not os.path.exists(img_path):
    os.makedirs(img_path)


# 填充图片大小
def get_padding_size(img):
    h, w, _ = img.shape
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


def read_data(path, w=width, h=height):
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


# 加载需要识别人脸数据
read_data(img_path)
# 加载陌生数据
for dirname in os.listdir(unknown_path):
    if dirname != sys.argv[1]:
        read_data("./data/" + dirname)
    else:
        pass


# 将图片数据与标签转换成数组
imgs = np.array(imgs)
labs = np.array([[0, 1] if lab == img_path else [1, 0] for lab in labs])

# 随机划分测试集与训练集
train_x, test_x, train_y, test_y = train_test_split(imgs, labs, test_size=0.3, random_state=0)

# 参数：图片数据的总数，图片的高、宽、通道
train_x = train_x.reshape(train_x.shape[0], width, height, 3)
test_x = test_x.reshape(test_x.shape[0], width, height, 3)

# 将数据转换成小于1的数
train_x = train_x.astype('float32') / 255.0
test_x = test_x.astype('float32') / 255.0

# 图片块，每次取50张图片
num_batch = len(train_x) // BATCH_SIZE

X = tf.placeholder(tf.float32, [None, width, height, 3])
y = tf.placeholder(tf.float32, [None, 2])

keep_prob = tf.placeholder(tf.float32)


def weight(input_):
    return tf.Variable(tf.random_normal(input_, stddev=0.01))


def bias(input_):
    return tf.Variable(tf.random_normal(input_))


def conv2d(x, w):
    return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')


def max_pool(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


def conv_net():
    # 第一层
    w1 = weight([3, 3, 3, 32])  # 卷积核大小(3,3)， 输入通道(3)， 输出通道(32)
    b1 = bias([32])
    # 卷积
    conv1 = tf.nn.relu(conv2d(X, w1) + b1)
    # 池化
    pool1 = max_pool(conv1)
    # 减少过拟合，随机让某些权重不更新
    drop1 = tf.nn.dropout(pool1, keep_prob=keep_prob)

    # 第二层
    w2 = weight([3, 3, 32, 64])
    b2 = bias([64])
    # 卷积
    conv2 = tf.nn.relu(conv2d(drop1, w2) + b2)
    # 池化
    pool2 = max_pool(conv2)
    # 减少过拟合，随机让某些权重不更新
    drop2 = tf.nn.dropout(pool2, keep_prob=keep_prob)

    # 第三层
    w3 = weight([3, 3, 64, 128])
    b3 = bias([128])
    # 卷积
    conv3 = tf.nn.relu(conv2d(drop2, w3) + b3)
    # 池化
    pool3 = max_pool(conv3)
    # 减少过拟合，随机让某些权重不更新
    drop3 = tf.nn.dropout(pool3, keep_prob=keep_prob)

    # 全连接层
    wc = weight([50 * 50 * 128, 512])
    bc = bias([512])
    drop4_flat = tf.reshape(drop3, [-1, 50 * 50 * 128])
    dense = tf.nn.relu(tf.matmul(drop4_flat, wc) + bc)
    drop4_flatten = tf.nn.dropout(dense, keep_prob=keep_prob)

    # 输出层
    wout = weight([512, 2])
    bout = bias([2])

    out = tf.add(tf.matmul(drop4_flatten, wout), bout)

    return out


# 使用dlib自带的frontal_face_detector作为我们的特征提取器
detector = dlib.get_frontal_face_detector()

pred = conv_net()
predict = tf.argmax(pred, 1)


def train():
    print(f"Train size:{len(train_x)}, test size:{len(test_x)}")

    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred, labels=y))

    train_step = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE).minimize(cross_entropy)
    # 比较标签是否相等，再求的所有数的平均值，tf.cast(强制转换类型)
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 数据保存器的初始化
    saver = tf.train.Saver()

    with tf.Session() as train_sess:

        train_sess.run(tf.global_variables_initializer())

        for epoch in range(1, MAX_EPOCH + 1):
            # 每次取128(batch_size)张图片
            for i in range(num_batch):
                batch_x = train_x[i * BATCH_SIZE: (i + 1) * BATCH_SIZE]
                batch_y = train_y[i * BATCH_SIZE: (i + 1) * BATCH_SIZE]
                # 开始训练数据，同时训练三个变量，返回三个数据
                _, loss, = train_sess.run([train_step, cross_entropy],
                                          feed_dict={X: batch_x, y: batch_y, keep_prob: 0.75})
            if epoch % DISPLAY_EPOCH == 0:
                # 获取测试数据的准确率
                train_acc = accuracy.eval({X: train_x, y: train_y, keep_prob: 1.0})
                print(f"Epoch {epoch} train acc: {train_acc:.5f} loss: {loss:.10f}")

        test_acc = accuracy.eval({X: test_x, y: test_y, keep_prob: 1.0})
        saver.save(train_sess, model_path)
        print(f"Validation acc : {test_acc}")
        print("Optimization complete!")
        print(f"Model save to {model_path}")
        sys.exit(0)


if __name__ == '__main__':
    os.system("find ./* -name '.DS_Store' -type f -delete")
    train()
