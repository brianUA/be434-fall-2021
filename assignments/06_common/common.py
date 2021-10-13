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

    parser.add_argument('file2',
                        help='files to input to find similarities',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='files to input to find similarities',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='specificy output file',
                        metavar='str',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
args = get_args()

file1 = set()
file2 = set()
for line in args.file1:
    for word in line.split():     
        file1.add(word)
#print(file1)
for line in args.file2:
    for word in line.split():     
        file2.add(word)
#print(file2)
output = file1.intersection(file2)

outstr = ""
for entry in output:
    outstr = outstr + entry + "\n"
print(outstr, file =args.outfile)



# --------------------------------------------------
if __name__ == '__main__':
    main()
