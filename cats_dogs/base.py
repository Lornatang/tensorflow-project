import os
import numpy as np
import tensorflow as tf
from PIL import Image

import train_test_split
import model

N_CLASSES = 2
IMG_W = 208  # resize the image, if the input image is too large, training will be very slow.
IMG_H = 208
RATIO = 0.2  # take 20% of dataset as validation data
BATCH_SIZE = 64
CAPACITY = 2000
MAX_STEP = 6000  # with current parameters, it is suggested to use MAX_STEP>10k
learning_rate = 0.0001  # with current parameters, it is suggested to use learning rate<0.0001


def run_training():
    # you need to change the directories to yours.
    train_dir = './data/train/'
    logs_train_dir = './logs/train/'
    logs_val_dir = './logs/val/'

    train, train_label, val, val_label = train_test_split.get_files(train_dir, RATIO)
    train_batch, train_label_batch = train_test_split.get_batch(train,
                                                                train_label,
                                                                IMG_W,
                                                                IMG_H,
                                                                BATCH_SIZE,
                                                                CAPACITY)
    val_batch, val_label_batch = train_test_split.get_batch(val,
                                                            val_label,
                                                            IMG_W,
                                                            IMG_H,
                                                            BATCH_SIZE,
                                                            CAPACITY)

    x = tf.placeholder(tf.float32, shape=[BATCH_SIZE, IMG_W, IMG_H, 3])
    y_ = tf.placeholder(tf.int16, shape=[BATCH_SIZE])

    logits = model.inference(x, BATCH_SIZE, N_CLASSES)
    loss = model.losses(logits, y_)
    acc = model.evaluation(logits, y_)
    train_op = model.training(loss, learning_rate)

    with tf.Session() as sess:
        saver = tf.train.Saver()
        sess.run(tf.global_variables_initializer())
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        summary_op = tf.summary.merge_all()
        train_writer = tf.summary.FileWriter(logs_train_dir, sess.graph)
        val_writer = tf.summary.FileWriter(logs_val_dir, sess.graph)

        try:
            for step in np.arange(MAX_STEP):
                if coord.should_stop():
                    break

                tra_images, tra_labels = sess.run([train_batch, train_label_batch])
                _, tra_loss, tra_acc = sess.run([train_op, loss, acc],
                                                feed_dict={x: tra_images, y_: tra_labels})
                if step % 50 == 0:
                    print("Step {}, train loss = {:.2f}, "
                          "train accuracy = {:.2f}%.".format(step, tra_loss, tra_acc * 100.0))
                    summary_str = sess.run(summary_op)
                    train_writer.add_summary(summary_str, step)

                if step % 200 == 0 or (step + 1) == MAX_STEP:
                    val_images, val_labels = sess.run([val_batch, val_label_batch])
                    val_loss, val_acc = sess.run([loss, acc],
                                                 feed_dict={x: val_images, y_: val_labels})
                    print("Step {}, val loss = {:.2f}, val accuracy = {:.2f}%.".format(step, val_loss, val_acc * 100.0))
                    summary_str = sess.run(summary_op)
                    val_writer.add_summary(summary_str, step)

                if step % 2000 == 0 or (step + 1) == MAX_STEP:
                    checkpoint_path = os.path.join(logs_train_dir, 'model.ckpt')
                    saver.save(sess, checkpoint_path, global_step=step)

        except tf.errors.OutOfRangeError:
            print("Done training -- epoch limit reached")
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

    # you need to change the directories to yours.
    train_dir = './data/train/'
    train, train_label = train_test_split.get_files(train_dir)
    image_array = get_one_image(train)

    with tf.Graph().as_default():
        batch_size = 1
        n_classes = 2

        image = tf.cast(image_array, tf.float32)
        image = tf.image.per_image_standardization(image)
        image = tf.reshape(image, [1, 208, 208, 3])

        logits = model.inference(image, batch_size, n_classes)

        logits = tf.nn.softmax(logits)

        x = tf.placeholder(tf.float32, shape=[208, 208, 3])

        # you need to change the directories to yours.
        logs_train_dir = './logs/train/'

        saver = tf.train.Saver()

        with tf.Session() as sess:

            print("Reading checkpoints...")
            ckpt = tf.train.get_checkpoint_state(logs_train_dir)
            if ckpt and ckpt.model_checkpoint_path:
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                saver.restore(sess, ckpt.model_checkpoint_path)
                print("Loading success, global_step is %s".format(global_step))
            else:
                print("No checkpoint file found")

            prediction = sess.run(logits, feed_dict={x: image_array})
            max_index = np.argmax(prediction)
            if max_index == 0:
                print("This is a cat with possibility {:.6f}.".format(prediction[:, 0]))
            else:
                print("This is a dog with possibility {:.6f}.".format(prediction[:, 1]))
