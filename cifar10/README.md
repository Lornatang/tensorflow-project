# How to use TensorFlow to process our own data?

1. read in data
2. make an input queue
3. generate batches
4. train
5. save model architecture and parameters
6. restore model architecture and parameters
7. test new data

# The data

Official Website: [look here](https://www.cs.toronto.edu/~kriz/cifar.html)

# The result

- I used 10k training steps, learning rate is 0.05, the performance on test dataset is 78.3%. While for the example on TensorFlow website, they used 100k training steps, got 83% on the test dataset. More can be done to improve this model.

# Usage:
    
## Training data:
    
```text
python main.py [-T | --train]
```

## Validation data:
    
```text
python main.py [-v | --validation]
```

## License

**MIT**

**Author: *[Shiyipaisizuo](https://github.com/shiyipaisizuo/tensorflow-project)*** 

**Audit: *[Shiyipaisizuo](https://github.com/shiyipaisizuo/tensorflow-project)***