#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-10-13
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='specificy output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
args = get_args()

fileset1 = set()
fileset2 = set()
for line in args.file1:
    for word in line.split():     
        fileset1.add(word)
#print(file1)
for line in args.file2:
    for word in line.split():     
        fileset2.add(word)
#print(file2)
output = fileset1.intersection(fileset2)

outstr = ""
for entry in output:
    outstr = outstr + entry + "\n"
print(outstr, file =args.outfile)



# --------------------------------------------------
if __name__ == '__main__':
    main()
