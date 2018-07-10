"""
    Building neural networks and computing.
"""

# Author: Changyu Liu <Shiyipaisizuo@gmail.com>
# Last modified: 2018-07-09
# LICENSE: MIT

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
from PIL import Image, ImageFilter


MAX_EPOCH = 25000  # Maximum number of epoch.
DISPLAY_STEP = 1000  # Output when running to 1000 integers.
BATCH_SIZE = 64  # How many pictures to train at one time.
IMAGE_WEIGHT = 28
IMAGE_HEIGHT = 28
N_CLASSES = 10
SAVE_PATH = '../../model/mnist/model.ckpt'
TRAIN_DIR = '/tmp/mnist/'


# The initialization function that defines the weight and offset is
# repeated later
def weight(shape):
    # The truncated normal distribution noise, with a standard deviation of 0.1,
    # is eliminated if it is greater than 2 standard deviations
    return tf.Variable(tf.truncated_normal(shape, stddev=0.1))


def bias(shape):
    # Offset, plus weak positive value, to avoid dead nodes
    return tf.Variable(tf.constant(0.1, shape=shape))


# Define the functions of convolution layer and pooling layer
def conv2d(x, w):
    # conv2d is a two-dimensional convolution, x is the input, and W is the parameter, such as [5,5,1,32].
    # 3 is channel, monochrome is 1, RGB is 3, and number 4 is the number of convolution kernels
    # SAME keeps the input and output size the SAME
    return tf.nn.conv2d(x,
                        w,
                        strides=[1, 1, 1, 1],
                        padding='SAME')


def max_pool_2x2(x):
    # Here we're going to go down in half vertical, and we're going to take
    # the one with the highest grayscale for each of the two, and we're going
    # to keep the most significant features
    return tf.nn.max_pool(x,
                          ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1],
                          padding='SAME')


# because convolution is going to take advantage of spatial information, we're going to convert the 1D to 2D,
# so we're going to convert the 1D data to the 28d data The final size of the picture is [-1,28,28,1] None represents
# an unlimited input dimension
X = tf.placeholder(tf.float32, [None, IMAGE_HEIGHT * IMAGE_WEIGHT])
y = tf.placeholder(tf.float32, [None, N_CLASSES])

x_image = tf.reshape(X, [-1, IMAGE_WEIGHT, IMAGE_HEIGHT, 1])

# Define the first convolution layer
W_conv1 = weight([5, 5, 1, 32])
b_conv1 = bias([32])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# Define the second convolution layer
W_conv2 = weight([5, 5, 32, 64])
b_conv2 = bias([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# The length of the side here has gone through two pools, only 1/4 left, and the number of convolution kernels is 64
# Therefore, there are also parameters 7*7*64
# Define a full connection layer
W_fc1 = weight([7 * 7 * 64, 1024])
b_fc1 = bias([1024])
# No matter how many samples you have, the second dimension is the fully
# expanded column of the picture
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# To reduce overfitting, add a mirroring layer below, which is controlled by passing a placeholder into keep_prob ratio
# this is to reduce overfitting by randomly discarding some data of nodes
# The effect of this rotation is very similar to that of regularities
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# Finally, the full connection layer is connected to an output layer of 10
W_fc2 = weight([1024, 10])
b_fc2 = bias([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# define the loss function, use the optimizer Adam, and set the learning rate to 1e-4
# The reduce_mean here is a common mean, and the global mean is default
# without axis
loss = tf.reduce_mean(-tf.reduce_sum(y * tf.log(y_conv),
                                     reduction_indices=[1]))
optimizer = tf.train.AdamOptimizer(1e-5).minimize(loss)

# Define evaluation accuracy
# Argmax is going to be the largest number in the Tensor
# equal returns True if it judges equality
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Save the model
saver = tf.train.Saver()
# Initialize all variables
init = tf.global_variables_initializer()


# Start training
def training():
    # Load the data
    mnist = input_data.read_data_sets(TRAIN_DIR, one_hot=True)
    with tf.Session() as sess:
        # Initialize all variables
        sess.run(init)

        for i in range(MAX_EPOCH + 1):
            batch = mnist.train.next_batch(BATCH_SIZE)
            if i % DISPLAY_STEP == 0:
                acc = accuracy.eval(feed_dict={X: batch[0],
                                               y: batch[1],
                                               keep_prob: 1.0})
                print(f"Step {i}, training accuracy {acc:.4f}")
            optimizer.run(feed_dict={
                X: batch[0],
                y: batch[1],
                keep_prob: 0.75})
        saver.save(sess, SAVE_PATH)
        print(f"Model save path to: {SAVE_PATH}")


def evaluate():
    # Load the data
    mnist = input_data.read_data_sets(TRAIN_DIR, one_hot=True)
    with tf.Session() as sess:
        # Initialize all variables
        sess.run(init)

        saver.restore(sess, SAVE_PATH)
        print(f"Model restore from : {SAVE_PATH}")
        acc = accuracy.eval(feed_dict={X: mnist.test.images,
                                       y: mnist.test.labels,
                                       keep_prob: 1.0})
        print(f"Acc: {acc:.4f}")


def read_data():
    im = Image.open('./data/2.png')  # 读取的图片所在路径，注意是28*28像素
    im = im.convert('L')
    tv = list(im.getdata())
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    return tva


result = read_data()


def test():
    with tf.Session() as sess:
        sess.run(init)
        # Using the model, the parameters are consistent with the previous code
        saver.restore(sess, SAVE_PATH)

        prediction = tf.argmax(y_conv, 1)
        predint = prediction.eval(
            feed_dict={
                X: [result],
                keep_prob: 1.0},
            session=sess)

        print("识别结果:", predint[0])
