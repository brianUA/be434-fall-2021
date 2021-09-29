#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-09-29
Purpose: Concatenate
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines in the output',
                        default=False,
                        action='store_true')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    for fh in args.files:
        counter = 1
        for line in fh:
            if args.number is False:
                print(line.rstrip('\n'))
            else:
                print("     " + str(counter) + "\t" + line.rstrip('\n'))
                counter += 1


# --------------------------------------------------
if __name__ == '__main__':
    main()
