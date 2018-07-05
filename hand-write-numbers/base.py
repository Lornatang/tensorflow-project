"""
    Based on the most classic mnist.
"""

# Author: Changyu Liu <Shiyipaisizuo@gmail.com>
# Last modified: 2018-07-04
# LICENSE: MIT

# Import the appropriate libraries
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Load mnist data
data = input_data.read_data_sets('./data/', one_hot=True)

# tf Graph input
X = tf.placeholder('float', [None, 784])
y = tf.placeholder('float', [None, 10])

# Store layers weight & bias
weights = {
    'w1': tf.Variable(tf.random_normal([784, 256])),
    'w2': tf.Variable(tf.random_normal([256, 256])),
    'w3': tf.Variable(tf.random_normal([256, 256])),
    'out': tf.Variable(tf.random_normal([256, 10]))
}
bias = {
    'b1': tf.Variable(tf.random_normal([256])),
    'b2': tf.Variable(tf.random_normal([256])),
    'b3': tf.Variable(tf.random_normal([256])),
    'out': tf.Variable(tf.random_normal([10]))
}


# Create cnn model
def cnn(x, w, b):
    """
    Args:
        x: input image
        w: neural network
        b: image biases
    Returns:
        Out: out with linear activation
        """
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, w['w1']), b['b1'])
    layer_1 = tf.nn.relu(layer_1)

    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, w['w2']), b['b2'])
    layer_2 = tf.nn.relu(layer_2)

    # Hidden layer with RELU activation
    layer_3 = tf.add(tf.matmul(layer_2, w['w3']), b['b3'])
    layer_3 = tf.nn.relu(layer_3)

    # Out with linear activation
    out = tf.add(tf.matmul(layer_3, w['out']), b['out'])

    return out


# Construct model
prediction = cnn(X, weights, bias)

# Define loss and optimizer
loss = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(
        logits=prediction, labels=y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(loss)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# 'Saver' op to save and restore all the variables
saver = tf.train.Saver()


def train(epoch):
    with tf.Session() as sess:
        # Run the initializer
        sess.run(init)

        # Loop over all batches
        for epoch in range(epoch):
            avg_cost = 0.
            total_batch = int(data.train.num_examples / 100)

            # Loop over all batches
            for i in range(total_batch):
                batch_x, batch_y = data.train.next_batch(100)

                # Run optimization op (backprop) and cost op (to get loss
                # value)
                _, c = sess.run([optimizer, loss], feed_dict={
                                X: batch_x, y: batch_y})

                avg_cost += c / total_batch

            # When epoch/1 == 0, display its
            if epoch % 1 == 0:
                print("Epoch: {}, cost:{:.9f}.".format(epoch + 1, avg_cost))
        print("Optimizer finished!")

        # Model path
        save_path = saver.save(sess, 'model/model.ckpt')
        print("Model save path---->{}".format(save_path))


def test():
    with tf.Session() as sess:
        # Load model
        saver.restore(sess, 'model/model.ckpt')

        # Test model
        correct_prediction = tf.equal(
            tf.argmax(
                prediction, 1), tf.argmax(
                y, 1))

        # Calculate accuracy
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        # Output accuracy
        print("Accuracy: {:.2f}%".format(accuracy.eval(
            {X: data.test.images, y: data.test.labels}) * 100))
