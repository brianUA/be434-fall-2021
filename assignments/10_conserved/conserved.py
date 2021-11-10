#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-11-09
Purpose: FInd the similarities between sequences.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    

    args = get_args()
    sequences = []
    for line in args.file:
        temp_list = []
        for char in line.strip():
            temp_list.append(char)
        sequences.append(temp_list)

    out_seq = ""
    for base in range(len(sequences[0])):
        temp_base = []
        for line in range(len(sequences)):
            temp_base.append(sequences[line][base])
            #print(temp_base)
        if all_same(temp_base):
            out_seq = out_seq + "|"
        else: 
            out_seq = out_seq + "X"
    
    #old attempt didn't work due to trying to compare within, ended up not always comparing last base.
    #for base in range(len(sequences[0])):
    #    for i in range(len(sequences)):
    #        if i < len(sequences)-1:
    #            if sequences[i][base] == sequences[i+1][base] if and sequences[i+2][base]:
    #                if len(out_seq) == len(sequences[0]):
    #                    break
    #                out_seq = out_seq + "|" 
    #            else:
    #                if len(out_seq) == len(sequences[0]):
    #                    break
    #                out_seq = out_seq + "X"
    for line in sequences:
        temp_line = ""
        for char in line:
            temp_line = temp_line + char
        print(temp_line)    
    print(out_seq)

def all_same(list1):
    return all(x == list1[0] for x in list1)   




# --------------------------------------------------
if __name__ == '__main__':
    main()
