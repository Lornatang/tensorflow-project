# Function instructions

## Directory tree
```text
├── __init__.py
├── __pycache__
│   └── base.cpython-37.pyc
├── base.py
├── base.pyc
├── data
│   ├── t10k-images-idx3-ubyte.gz
│   ├── t10k-labels-idx1-ubyte.gz
│   ├── train-images-idx3-ubyte.gz
│   └── train-labels-idx1-ubyte.gz
├── introduce.md
├── main.py
└── model
    ├── checkpoint
    ├── model.ckpt.data-00000-of-00001
    ├── model.ckpt.index
    └── model.ckpt.meta
```


### def train(epoch)

```python
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
```

### def test()

```python
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
```

### def main()

```python
import argparse
def main():
    parser = argparse.ArgumentParser()
    # Parameter cannot be repeated
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--train",
        help="Starting training mnist",
        action="store_true")
    group.add_argument(
        "--test",
        help="Calculate accuracy",
        action="store_true")
    args = parser.parse_args()
    if args.train:
        base.train(50)
    elif args.test:
        base.test()
    else:
        args.format_usage()
```

#### Usage: 

**python main.py --train**

*You 'll see*
```text
Epoch: 1, cost:1465.749074652.
Epoch: 2, cost:358.950801634.
Epoch: 3, cost:215.583005248.
Epoch: 4, cost:143.596455115.
Epoch: 5, cost:100.857781702.
Epoch: 6, cost:72.147256477.
Epoch: 7, cost:51.398675599.
Epoch: 8, cost:36.388558753.
Epoch: 9, cost:25.647963873.
Epoch: 10, cost:18.697037627.
Epoch: 11, cost:14.011822952.
Epoch: 12, cost:11.864846532.
Epoch: 13, cost:9.678910431.
Epoch: 14, cost:8.239972835.
Epoch: 15, cost:7.259532100.
Epoch: 16, cost:6.497665578.
Epoch: 17, cost:5.505862782.
Epoch: 18, cost:5.848468989.
Epoch: 19, cost:6.275718566.
Epoch: 20, cost:4.614883631.
Epoch: 21, cost:3.559349296.
Epoch: 22, cost:4.711895169.
Epoch: 23, cost:4.970205748.
Epoch: 24, cost:3.949323646.
Epoch: 25, cost:3.361469757.
Epoch: 26, cost:4.426729311.
Epoch: 27, cost:3.666941071.
Epoch: 28, cost:2.743820582.
Epoch: 29, cost:3.947338344.
Epoch: 30, cost:2.897383927.
Epoch: 31, cost:3.100600044.
Epoch: 32, cost:3.383983951.
Epoch: 33, cost:3.303998014.
Epoch: 34, cost:2.977089446.
Epoch: 35, cost:2.814323372.
Epoch: 36, cost:3.331458229.
Epoch: 37, cost:2.389651632.
Epoch: 38, cost:1.903855870.
Epoch: 39, cost:3.342399193.
Epoch: 40, cost:3.074553787.
Epoch: 41, cost:2.701295445.
Epoch: 42, cost:2.231522787.
Epoch: 43, cost:2.611505464.
Epoch: 44, cost:1.872499419.
Epoch: 45, cost:2.452242370.
Epoch: 46, cost:2.270775151.
Epoch: 47, cost:2.393156816.
Epoch: 48, cost:1.931829598.
Epoch: 49, cost:1.763150141.
Epoch: 50, cost:2.725590840.
Optimizer finished!
Model save path---->model/model.ckpt
```

**python main.py --test**

*You 'll see*
```text
Accuracy: 96.45%
```

- Author: *[Shiyipaisizuo](https://github.com/shiyipaisizuo)*
- Audit: *[Shiyipaisizuo](https://github.com/shiyipaisizuo)*

## License

**MIT**