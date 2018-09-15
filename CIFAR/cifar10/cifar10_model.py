"""Model class for Cifar10 Dataset.

# author: shiyipaisizuo
# contact: shiyipaisizuo@gmail.com
# file: cifar10_model.py
# time: 2018/9/15 11:23
# license: MIT

# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""

import tensorflow as tf

import base


class ResNetCifar10(base.ResNet):
    """Cifar10 model with ResnetV1 and basic residual"""

    def __init__(self,
                 num_layers,
                 is_training,
                 batch_norm_decay,
                 batch_norm_epsilon,
                 data_dormat='channels_first'):
        super(ResNetCifar10, self).__init__(
            is_training,
            data_dormat,
            batch_norm_decay,
            batch_norm_epsilon
        )
        self.n = (num_layers - 2) // 6
        self.num_classes = 10 + 1
        self.filters = [16, 16, 32, 64]
        self.strides = [1, 2, 2]

    def forward_pass(self, x, input_data_format='channels_last'):
        """Build the core model within the graph"""
        if self._data_format != input_data_format:
            if input_data_format == 'channels_last':
                x = tf.transpose(x, [0, 3, 1, 2])
            else:
                x = tf.transpose(x, [0, 2, 3, 1])

        x = x / 128 - 1

        x = self._conv(x, 3, 16, 1)
        x = self._batch_norm(x)
        x = self._relu(x)

        res_func = self._residual_v1

        for i in range(3):
            with tf.name_scope('stage'):
                for j in range(self.n):
                    if j == 0:
                        x = res_func(x, 3, self.filters[i], self.filters[i + 1],
                                     self.strides[i])
                    else:
                        x = res_func(x, 3, self.filters[i + 1], self.filters[i + 1], 1)

        x = self._global_avg_pool(x)
        x = self._fully_connected(x, self.num_classes)

        return x
