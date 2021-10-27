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
    list1 = []
    fileset2 = set()
    list2 = []
    for line in args.file1:
        nospace = line.replace(" ", "").strip().replace(".", "").replace(",", "")
        #print(line.rstrip(),nospace)
        for char in range(0,len(nospace)):
            fileset1.add(nospace[char:(char+args.kmer)])
            list1.append(nospace[char:(char+args.kmer)])
    #print(fileset1)
    for line in args.file2:
        nospace = line.replace(" ", "").strip().replace(".", "").replace(",", "")
        for char in range(0,len(nospace)):
            fileset2.add(nospace[char:(char+args.kmer)])
            list2.append(nospace[char:(char+args.kmer)])
    #print(fileset2)
    kmers_set = fileset1.intersection(fileset2)

    final_kmers = set()
    #print(list1)
    for item in kmers_set:
        if len(item) == args.kmer:
            final_kmers.add(item)

    for item in final_kmers:
        print('{0:10}{1:6}{2:6}'.format(item, list1.count(item), list2.count(item)))

                



# --------------------------------------------------
if __name__ == '__main__':
    main()
