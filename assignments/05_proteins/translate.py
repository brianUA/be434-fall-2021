#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-10-06
Purpose: Translate dna into codons
"""

import argparse
from pprint import pprint

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA or RNA to translate')

    parser.add_argument('-c',
                        '--codons',
                        help='Codons to look for',
                        metavar='FILE',
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
    #for line in args.codons:
     #   print(line.rstrip().split())
    codon_table = {}
    for line in args.codons:
        entry = line.rstrip().split()
        codon_table[entry[0]] = (entry[1])
    k = 3
    seq = args.sequence
    outstr = ''
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        if codon_table.get(codon.upper()) == None:
            outstr = outstr + '-'
        else:
            outstr = outstr + (codon_table.get(codon.upper()))

    print("Output written to \"" + args.outfile + "\"." )
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(outstr)
    out_fh.close()
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
