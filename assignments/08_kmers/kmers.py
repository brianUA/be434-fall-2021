#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-10-27
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1 ',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='kmer size (default: 3)',
                        metavar='int',
                        type=int,
                        default=3)
    args = parser.parse_args()
    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')


    return args


# --------------------------------------------------
def main():

    args = get_args()

    fileset1 = set()
    fileset2 = set()
    for line in args.file1:
        for word in line.split():
            fileset1.add(word)
    for line in args.file2:
        for word in line.split():
            fileset2.add(word)
    kmers = fileset1.intersection(fileset2)
    for kmer in kmers:
        print(kmer[0:args.kmer])
                



# --------------------------------------------------
if __name__ == '__main__':
    main()
