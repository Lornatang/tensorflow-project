"""
# author: shiyipaisizuo
# contact: shiyipaisizuo@gmail.com
# file: validation.py
# time: 2018/9/11 19:02
# license: MIT
"""

from PIL import Image
import argparse

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# log
tf.logging.set_verbosity(tf.logging.DEBUG)

data = input_data.read_data_sets("../data/MNIST/MNIST/", one_hot=True)  # Load data

# Parameters
parser = argparse.ArgumentParser("Tensorflow mnist")
parser.add_argument('--learning_rate', default=0.001)
parser.add_argument('--epoch', default=100)
parser.add_argument('--batch_size', default=128)
parser.add_argument('--dis_epoch', default=2)
# Network Parameters
parser.add_argument('--img_size', default=784)
parser.add_argument('--classes', default=10)
parser.add_argument('--dropout', default=0.75)
parser.add_argument('--model_path', default='../../models/tensorflow/MNIST/MNIST/MNIST.ckpt')
args = parser.parse_args()

# tf Graph input
X = tf.placeholder(tf.float32, [None, args.img_size])
y = tf.placeholder(tf.float32, [None, args.classes])
keep_prob = tf.placeholder(tf.float32)  # drop(keep probability)


# Create model
def conv2d(image, w, b):
    return tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(image, w, strides=[1, 1, 1, 1], padding='SAME'), b))


def max_pooling(image, k):
    return tf.nn.max_pool(image, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='SAME')


weights = {
    'wc1': tf.Variable(tf.random_normal([3, 3, 1, 64])),
    'wc2': tf.Variable(tf.random_normal([3, 3, 64, 128])),
    'wd1': tf.Variable(tf.random_normal([7 * 7 * 128, 1024])),
    'out': tf.Variable(tf.random_normal([1024, args.classes]))
}
biases = {
    'bc1': tf.Variable(tf.random_normal([64])),
    'bc2': tf.Variable(tf.random_normal([128])),
    'bd1': tf.Variable(tf.random_normal([1024])),
    'out': tf.Variable(tf.random_normal([args.classes]))
}


def conv_net(x, _weights, _biases, _dropout):
    # Layer 1
    x = tf.reshape(x, [-1, 28, 28, 1])
    conv1 = conv2d(x, _weights['wc1'], _biases['bc1'])
    conv1 = max_pooling(conv1, k=2)
    conv1 = tf.nn.dropout(conv1, keep_prob=_dropout)
    # Layer 2
    conv2 = conv2d(conv1, _weights['wc2'], _biases['bc2'])
    conv2 = max_pooling(conv2, k=2)
    conv2 = tf.nn.dropout(conv2, keep_prob=_dropout)
    # Fully Connected
    dense1 = tf.reshape(conv2, [-1, _weights['wd1'].get_shape().as_list()[0]])
    dense1 = tf.nn.relu(tf.add(tf.matmul(dense1, _weights['wd1']), _biases['bd1']))
    dense1 = tf.nn.dropout(dense1, _dropout)
    out = tf.add(tf.matmul(dense1, _weights['out']), _biases['out'])

    return out


# Construct model
pred = conv_net(X, weights, biases, keep_prob)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=pred))
optimizer = tf.train.AdamOptimizer(learning_rate=args.learning_rate).minimize(cost)

# Evaluate model
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))


def imageprepare():
    """
    This function returns the pixel values.
    The imput is a png file location.
    """
    file_name = '../data/MNIST/MNIST/test/2.jpg'  # 导入自己的图片地址
    # in terminal 'mogrify -format png *.jpg' convert jpg to png
    im = Image.open(file_name).convert('L')
    tv = list(im.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    # print(tva)
    return tva

    # Define the model (same as when creating the model file)


result = imageprepare()

init_op = tf.initialize_all_variables()

"""
Load the model2.ckpt file
file is stored in the same directory as this python script is started
Use the model to predict the integer. Integer is returend as list.

Based on the documentatoin at
https://www.tensorflow.org/versions/master/how_tos/variables/index.html
"""
saver = tf.train.Saver()


def main(_):
    tf.app.run(main=main, agrv=[sys.argv[0]])


with tf.Session() as sess:
    saver.restore(sess, '../../models/tensorflow/MNIST/MNIST/MNIST.ckpt')  # 这里使用了之前保存的模型参数
    # print ("Model restored.")

    prediction = tf.argmax(pred, 1)
    predint = prediction.eval(feed_dict={X: [result], keep_prob: 1.0}, session=sess)

    print('recognize result:')
    print(predint[0])
