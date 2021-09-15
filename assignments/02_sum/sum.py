#!/usr/bin/env python3
"""
Author : Brian Scott (brianscott@email.arizona.edu)
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add integers from input',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('integers',
                        metavar='int',
                        nargs='+',
                        type=int,
                        help='Integers to add')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main Script to sum"""

    args = get_args()
    if len(args.integers) == 1:
        print(str(args.integers[0]) + " = " + str(args.integers[0]))
    else: 
        print(' + '.join(map(str, args.integers)) + " = " + str(sum(args.integers)))



# --------------------------------------------------
if __name__ == '__main__':
    main()
