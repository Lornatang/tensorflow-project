from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf


mnist = input_data.read_data_sets("/tmp/mnist/", one_hot=True)


# 定义权重和偏置的初始化函数，后面会重复调用
def weight_variable(shape):
    # 截断的正态分布噪声，标准差为0.1，这里值大于2倍标准差的都被干掉了
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    # 偏置，加微弱的正值，避免死亡节点
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 定义卷积层、池化层的函数
def conv2d(x, W):
    # conv2d是二维卷积，x是输入，W是参数，如[5,5,1,32]前面两个是尺寸
    # 第三个是channel，单色是1，RGB是3，第4个是卷积核数量
    # SAME是保持输入输出尺寸一样
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # 这里都是横竖降成一半，每二个取灰度最大的那个，保留最显著的特征
    return tf.nn.max_pool(
        x, ksize=[
            1, 2, 2, 1], strides=[
            1, 2, 2, 1], padding='SAME')


# 因为卷积会利用到空间信息，所以要将1D的转化为2D的，所以要把数据给的1*784转为28*28d的
# 图片最终尺寸为[-1,28,28,1]，-1是样本不固定的意思，最后的1是通道数量
# None表示不限输入维度
x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])

x_image = tf.reshape(x, [-1, 28, 28, 1])

# 定义第一个卷积层
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
# 激活函数用的relu
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# 定义第二个卷积层
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
# 这里的边长经历了两个池化，只剩1/4，卷积核数量为64
# 故共还有参数7*7*64
h_pool2 = max_pool_2x2(h_conv2)

# 接下来开始连接一个全连接层
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
# 不管你有多少个样本数量，反正第二维就是图片全展开的列
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 为了减少过拟合，下面加一个Dropout层，这个是通过一个placeholder传入keep_prob比率来控制
# 这个是通过随机丢弃一部分节点的数据来减轻过拟合
# 这个Dropout的作用和正则很相似
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 最后把全连接层连接到一个个数为10的输出层
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# 定义损失函数，使用优化器Adam，学习率设为1e-4
# 这里的reduce_mean就是普通的均值，不传axis就默认全局均值
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv),
                                              reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# 定义评测准确率
# tf.argmax就是从一个Tensor中找到值最大的序号
# equal判断相等就返回True
# tf.cast把correct_prediction的bool转成float32，e.g.[1,0,1,0]
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 开始训练，初始化所有参数
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        # batch队列
        batch = mnist.train.next_batch(50)
        if i % 100 == 0:
            # t.eval()时，等价于：tf.get_default_session().run(t)
            # accuracy run不影响训练
            train_accuracy = accuracy.eval(feed_dict={x: batch[0],
                                                      y_: batch[1],
                                                      keep_prob: 1.0})
            print("step %d, training accuracy %g" % (i, train_accuracy))
    # train_step run就会改变值了
        train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

    print("test accuracy :%g" % accuracy.eval(feed_dict={x: mnist.test.images,
                                                         y_: mnist.test.labels,
                                                         keep_prob: 1.0}))
