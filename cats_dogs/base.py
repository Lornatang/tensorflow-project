"""
    Start training and verifying accuracy
"""

# Author: Kevin <https://github.com/kevin28520>
# Last modified: 2018-07-05
# LICENSE: MIT

import os
import numpy as np
import tensorflow as tf
from PIL import Image

import train_test_split
import model

N_CLASSES = 2  # dogs and cats
IMG_W = 208  # resize the image, if the input image is too large, training will be very
IMG_H = 208
BATCH_SIZE = 64
CAPACITY = 2000
MAX_STEP = 15000
# with current parameters, it is suggested to use learning rate<0.0001
learning_rate = 0.0001


def run_training():
    # Set the training directory, test logs, and training logs.
    train_dir = './data/train/'
    logs_train_dir = './logs/train/'
    logs_test_dir = './logs/test/'

    # # take 20% of dataset as validation data
    X_train, y_train, X_test, y_test = train_test_split.get_files(
        train_dir, 0.3)

    # Gets the batch size
    train_batch, train_label_batch = train_test_split.get_batch(
        X_train, y_train, IMG_W, IMG_H, BATCH_SIZE, CAPACITY)
    val_batch, val_label_batch = train_test_split.get_batch(X_test,
                                                            y_test,
                                                            IMG_W,
                                                            IMG_H,
                                                            BATCH_SIZE,
                                                            CAPACITY)

    X = tf.placeholder(tf.float32, shape=[BATCH_SIZE, IMG_W, IMG_H, 3])
    y = tf.placeholder(tf.int16, shape=[BATCH_SIZE])

    logits = model.inference(X, BATCH_SIZE, N_CLASSES)
    loss = model.losses(logits, y)
    accuracy = model.evaluation(logits, y)
    train_op = model.trainning(loss, learning_rate)

    with tf.Session() as sess:
        saver = tf.train.Saver()
        sess.run(tf.global_variables_initializer())
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        summary_op = tf.summary.merge_all()
        train_writer = tf.summary.FileWriter(logs_train_dir, sess.graph)
        val_writer = tf.summary.FileWriter(logs_test_dir, sess.graph)

        try:
            for step in np.arange(MAX_STEP):
                if coord.should_stop():
                    break
                tra_images, tra_labels = sess.run(
                    [train_batch, train_label_batch])
                _, tra_loss, tra_acc = sess.run([train_op, loss, accuracy], feed_dict={
                    X: tra_images, y: tra_labels})
                if step % 50 == 0:
                    print(
                        'Step %d, train loss = %.2f, train accuracy = %.2f%%' %
                        (step, tra_loss, tra_acc * 100.0))
                    summary_str = sess.run(summary_op)
                    train_writer.add_summary(summary_str, step)

                if step % 200 == 0 or (step + 1) == MAX_STEP:
                    val_images, val_labels = sess.run(
                        [val_batch, val_label_batch])
                    val_loss, val_acc = sess.run([loss, accuracy], feed_dict={
                        X: val_images, y: val_labels})
                    print(
                        '**  Step %d, val loss = %.2f, val accuracy = %.2f%%  **' %
                        (step, val_loss, val_acc * 100.0))
                    summary_str = sess.run(summary_op)
                    val_writer.add_summary(summary_str, step)

                if step % 2000 == 0 or (step + 1) == MAX_STEP:
                    checkpoint_path = os.path.join(
                        logs_train_dir, 'model.ckpt')
                    saver.save(sess, checkpoint_path, global_step=step)

        except tf.errors.OutOfRangeError:
            print('Done training -- epoch limit reached')
        finally:
            coord.request_stop()
        coord.join(threads)


def get_one_image(train):
    """
    Randomly pick one image from training data

    Return: ndarray
    """
    n = len(train)
    ind = np.random.randint(0, n)
    img_dir = train[ind]

    image = Image.open(img_dir)
    image = image.resize([208, 208])
    image = np.array(image)

    return image


def evaluate_one_image():
    """
        Test one image against the saved models and parameters
    """

    # Set train directory.
    train_dir = './data/train/'
    train, train_label = train_test_split.get_files(train_dir)
    image_array = get_one_image(train)

    with tf.Graph().as_default():
        image = tf.cast(image_array, tf.float32)
        image = tf.image.per_image_standardization(image)
        image = tf.reshape(image, [1, 208, 208, 3])

        logits = model.inference(image, 1, 2)

        logits = tf.nn.softmax(logits)

        X = tf.placeholder(tf.float32, shape=[208, 208, 3])

        # Set train log directory.
        logs_train_dir = './logs/train/'

        saver = tf.train.Saver()

        with tf.Session() as sess:

            print("Reading checkpoints...")
            ckpt = tf.train.get_checkpoint_state(logs_train_dir)
            if ckpt and ckpt.model_checkpoint_path:
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                saver.restore(sess, ckpt.model_checkpoint_path)
                print("Loading success, global_step is {}.".format(global_step))
            else:
                print("No checkpoint file found")

            prediction = sess.run(logits, feed_dict={X: image_array})
            max_index = np.argmax(prediction)
            if max_index == 0:
                print("This is a cat with possibility {:.6f}".format(prediction[:, 0]))
            else:
                print("This is a dog with possibility {:.6f}.".format(prediction[:, 1]))
