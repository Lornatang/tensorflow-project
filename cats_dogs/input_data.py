"""
    Classify the data that needs training.
"""

# Author: Changyu Liu <Shiyipaisizuo@gmail.com>
# Last modified: 2018-07-05
# LICENSE: MIT

import tensorflow as tf
import numpy as np
import os


# data directory
train_dir = './data/train/'
BATCH_SIZE = 2
CAPACITY = 256
IMG_W = 208
IMG_H = 208


def get_files(file_dir):
    """
        Get the data you need to train
    ====================
    Args:
        file_dir: file directory
    ====================
    Returns:
        list of images and labels
    """
    cats = []
    label_cats = []
    dogs = []
    label_dogs = []
    for file in os.listdir(file_dir):
        name = file.split(sep='.')
        if name[0] == 'cat':
            cats.append(file_dir + file)
            label_cats.append(0)
        else:
            dogs.append(file_dir + file)
            label_dogs.append(1)
    print("There are {} cats\nThere are {} dogs".format(len(cats), len(dogs)))

    img_list = np.hstack((cats, dogs))
    labels_list = np.hstack((label_cats, label_dogs))

    temp = np.array([img_list, labels_list])
    temp = temp.transpose()
    np.random.shuffle(temp)

    img_list = list(temp[:, 0])
    labels_list = list(temp[:, 1])
    labels_list = [int(k) for k in labels_list]

    return img_list, labels_list


def get_batch(image, labels, image_W, image_H, batch_size, capacity):
    """
        Get the batch training size
    ====================
    Args:
        image: list type
        labels: list type
        image_W: image width
        image_H: image height
        batch_size: batch size
        capacity: the maximum elements in queue
    ====================
    Returns:
        image_batch: 4D tensor [batch_size, width, height, 3], dtype=tf.float32
        label_batch: 1D tensor [batch_size], dtype=tf.int32
    """

    image = tf.cast(image, tf.string)
    labels = tf.cast(labels, tf.int32)

    # make an input queue
    input_queue = tf.train.slice_input_producer([image, labels])

    labels = input_queue[1]
    image_contents = tf.read_file(input_queue[0])
    image = tf.image.decode_jpeg(image_contents, channels=3)

    image = tf.image.resize_image_with_crop_or_pad(image, image_W, image_H)

    # if you want to test the generated batches of images, you might want to
    # comment the following line.
    image = tf.image.per_image_standardization(image)

    img_batch, labels_batch = tf.train.batch([image, labels],
                                             batch_size=batch_size,
                                             num_threads=64,
                                             capacity=capacity)

    labels_batch = tf.reshape(labels_batch, [batch_size])
    img_batch = tf.cast(img_batch, tf.float32)

    return img_batch, labels_batch


image_list, label_list = get_files(train_dir)
image_batch, label_batch = get_batch(
    image_list, label_list, IMG_W, IMG_H, BATCH_SIZE, CAPACITY)

with tf.Session() as sess:
    i = 0
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    try:
        while not coord.should_stop() and i < 1:

            img, label = sess.run([image_batch, label_batch])

            # just test one batch
            for j in np.arange(BATCH_SIZE):
                print("label: {}".format(label[j]))
            i += 1

    except tf.errors.OutOfRangeError:
        print("Done!")
    finally:
        coord.request_stop()
    coord.join(threads)
