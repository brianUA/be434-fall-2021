#!/usr/bin/env python3
"""
Author : brian scott <brianscott@email.arizona.edu>
Date   : 2021-11-01
Purpose: Rock the Casbah
"""

import argparse
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='SPlit interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='specificy output directory',
                        metavar='str',
                        default="split")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()




# --------------------------------------------------
if __name__ == '__main__':
    main()
