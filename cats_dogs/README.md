# How to use TensorFlow to process our own data?

1. read in data
2. make an input queue
3. generate batches
4. train
5. save model architecture and parameters
6. restore model architecture and parameters
7. test new data

# The data

- Data: The cats vs. dogs dataset from Kaggle were used
- Download link: https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data

# The goal

- the goal of this project is to show how to use Tensorflow to process our own data.
- only 2 conv layers are used here, more complex and powerful models will be covered in the future 

# Usage:
    
## Training data:
    
```text
python main.py [-T | --train]
```

## Validation data:
    
```text
python main.py [-v | --validation]
```

- Author: *[Kevin](https://github.com/kevin28520)*
- Audit: *[Shiyipaisizuo](https://github.com/shiyipaisizuo)*

## License

**MIT**