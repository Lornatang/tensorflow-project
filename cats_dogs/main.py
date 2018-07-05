"""
    Main function parameter.
"""

# Author: Changyu Liu <Shiyipaisizuo@gmail.com>
# Last modified: 2018-07-05
# LICENSE: MIT

import argparse
import base


def main():
    parser = argparse.ArgumentParser()
    # Parameter cannot be repeated
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--train",
        "-T",
        help="Starting training mnist",
        action="store_true")
    group.add_argument(
        "--validation",
        "-V",
        help="Calculate accuracy",
        action="store_true")
    args = parser.parse_args()
    if args.train:
        base.run_training()
    elif args.validation:
        base.evaluate_one_image()


if __name__ == '__main__':
    main()
