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

    parser.add_argument('files',
                        help='files to input to find similarities',
                        metavar='FILE',
                        nargs='+',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='specificy output file',
                        metavar='str',
                        type=str,
                        default="out.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
args = get_args()

file1 = set()
file2 = set()
fh1 = args.files[0]
for line in fh1:
    for word in line.split():     
        file1.add(word)
#print(file1)
fh2 = args.files[1]
for line in fh2:
    for word in line.split():     
        file2.add(word)
#print(file2)
output = file1.intersection(file2)

out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
for entry in output:
    entry = entry + "\n"
    out_fh.write(entry)

out_fh.close()





# --------------------------------------------------
if __name__ == '__main__':
    main()
