"""
    Classify the data that needs training.
"""

# Author: Changyu Liu <Shiyipaisizuo@gmail.com>
# Last modified: 2018-07-05
# LICENSE: MIT

import tensorflow as tf
import numpy as np
import os
import math


def get_files(file_dir, ratio):
    """
    Get files for data cutting
    ===================
    Args:
        file_dir: you will get data directory
        ratio: data set to test
    ====================
    Return:
        list of images and labels
    """

    # Create list of cats and dogs
    cats = []
    label_cats = []
    dogs = []
    label_dogs = []

    # Return a list containing the names of the files in the directory.
    for file in os.listdir(file_dir):
        name = file.split(sep='.')
        if name[0] == 'cat':
            cats.append(file_dir + file)
            label_cats.append(0)
        else:
            dogs.append(file_dir + file)
            label_dogs.append(1)
    print("There are {} cats.".format(len(cats)))
    print("There are {} dogs.".format(len(dogs)))

    image_list = np.hstack((cats, dogs))
    label_list = np.hstack((label_cats, label_dogs))

    temp = np.array([image_list, label_list])
    temp = temp.transpose()
    np.random.shuffle(temp)

    all_image_list = temp[:, 0]
    all_label_list = temp[:, 1]

    n_sample = len(all_label_list)
    # number of validation samples
    n_val = math.ceil(n_sample * ratio)
    # number of training samples
    n_train = n_sample - n_val

    X_train = all_image_list[0:n_train]
    y_train = all_label_list[0:n_train]
    y_train = [int(float(i)) for i in y_train]
    X_test = all_image_list[n_train:-1]
    y_test = all_label_list[n_train:-1]
    y_test = [int(float(i)) for i in y_test]

    return X_train, X_test, y_train, y_test


def get_batch(image, label, image_W, image_H, batch_size, capacity):
    """
    Get batch training
    ====================
    Args:
        image: list type
        label: list type
        image_W: image width
        image_H: image height
        batch_size: batch size
        capacity: the maximum elements in queue
    ====================
    Returns:
        image_batch: 4D tensor [batch_size, width, height, 3], dtype=tf.float32
        label_batch: 1D tensor [batch_size], dtype=tf.int32
    """

    # A Tensor or SparseTensor with same shape as x.
    image = tf.cast(image, tf.string)
    label = tf.cast(label, tf.int32)

    # make an input queue
    # A list of tensors, one for each element of tensor_list. If the tensor in \
    # tensor_list has shape [N, a, b, .., z], then the corresponding output \
    # tensor will have shape [a, b, ..., z].
    input_queue = tf.train.slice_input_producer([image, label])

    label = input_queue[1]

    # read image and decode images
    image_contents = tf.read_file(input_queue[0])
    image = tf.image.decode_jpeg(image_contents, channels=3)

    # Transform the image size
    image = tf.image.resize_image_with_crop_or_pad(image, image_W, image_H)

    # The standardized image with same shape as image.
    image = tf.image.per_image_standardization(image)

    image_batch, label_batch = tf.train.batch([image, label],
                                              batch_size=batch_size,
                                              num_threads=64,
                                              capacity=capacity)
    # A list or dictionary of tensors with the same types as tensors (except \
    # if the input is a list of one element, then it returns a tensor, not a \
    # list).
    label_batch = tf.reshape(label_batch, [batch_size])
    image_batch = tf.cast(image_batch, tf.float32)

    return image_batch, label_batch
