"""
# author: shiyipaisizuo
# contact: shiyipaisizuo@gmail.com
# file: train.py
# time: 2018/8/16 16:10
# license: MIT
"""


import tensorflow as tf
from tensorflow.contrib import slim
import numpy as np

import utils



def AlexNet(x_input):
    with slim.arg_scope([slim.conv2d, slim.fully_connected],
                        activation_fn=tf.nn.relu,
                        weights_initializer=tf.truncated_normal_initializer(mean=0.0, stddev=0.01),
                        weights_regularizer=slim.l2_regularizer(0.0005)):
        # layer 1
        net = slim.conv2d(x_input, 96, [11, 11], padding="VALID", stride=4, scope="conv_1")
        net = tf.nn.local_response_normalization(net, depth_radius=5, bias=2, alpha=0.0001, beta=0.75)
        net = slim.max_pool2d(net, [3, 3], 2, scope="pool_1")
        # layer 2
        net = slim.conv2d(net, 256, [5, 5], scope="conv_2")
        net = tf.nn.local_response_normalization(net, depth_radius=5, bias=2, alpha=0.0001, beta=0.75)
        net = slim.max_pool2d(net, [3, 3], 2, scope="pool_2")
        # layer 3 4
        net = slim.repeat(net, 2, slim.conv2d, 384, [3, 3], scope="conv_3_4")
        # layer 5
        net = slim.conv2d(net, 256, [3, 3], scope="conv_5")
        net = slim.max_pool2d(net, [3, 3], 2, scope="pool_5")
        # flatten
        net = slim.flatten(net, scope="flatten")
        # layer 6
        net = slim.fully_connected(net, 4096, scope="fc_6")
        net = slim.dropout(net, keep_prob=0.5)
        # layer 7
        net = slim.fully_connected(net, 4096, scope="fc_7")
        net = slim.dropout(net, keep_prob=0.5)
        # output
        net = slim.fully_connected(net, 2, scope="output", activation_fn=None)

        return net


# 构建输入、输出、loss、train_op等
x_inputs = tf.placeholder(shape=[None, 128, 128, 3], dtype=tf.float32)
y_labels = tf.placeholder(shape=[None, 2], dtype=tf.float32)

train_datasets = utils.LoadDataset("../data/catdog/train")

with tf.Session(config=tf.ConfigProto(device_count={'gpu': 0})) as sess:
    sess.run(tf.global_variables_initializer())

    # model
    predicts = AlexNet(x_inputs)
    # loss function
    loss = tf.losses.softmax_cross_entropy(y_labels, predicts)
    # train op
    optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(loss)
    # accuracy
    correct_prediction = tf.equal(tf.argmax(predicts, 1), tf.argmax(y_labels, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    for epoch in range(20):
        images, labels = train_datasets.reads(batch_size=128)
        accuracy, optimizer, loss = sess.run([accuracy, optimizer, loss], feed_dict={x_inputs: images, y_labels: labels})
        print(f"Acc: {accuracy} Loss: {loss}")
