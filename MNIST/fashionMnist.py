"""
# author: shiyipaisizuo
# contact: shiyipaisizuo@gmail.com
# file: fashionMnist.py
# time: 2018/9/11 15:00
# license: MIT
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

tf.logging.set_verbosity(tf.logging.DEBUG)

mnist = input_data.read_data_sets("../data/mnist/", one_hot=True)  # Load data

# Parameters
learning_rate = 0.001
MAX_STEP = 1000
batch_size = 128
display_step = 1

# Network Parameters
n_input = 784  # MNIST data input(image shape = [28,28])
n_classes = 10  # MNIST total classes (0-9digits)
dropout = 0.75  # probability to keep units
