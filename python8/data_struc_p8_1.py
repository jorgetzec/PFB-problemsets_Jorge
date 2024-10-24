#!/usr/bin/env python3

# in bash terminal
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_08.fasta

# Problem 1
import sys
import re
from collections import Counter
from pprint import pprint
records = {}
sequence=''
# this works too

# with open(sys.argv[1], 'r') as fasta_file:
#     for line in fasta_file:
#         line = line.rstrip()
#         if line.startswith('>'):
#             header = re.search(r'>(\S+)(.+)', line)
#             idseq = header.group(1)
#             if idseq is not records:
#                 records[idseq]= ''
#         else:
#             sequence+=line
#             records[idseq]= Counter(sequence)
#     print(records)
                

with open(sys.argv[1], 'r') as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        if line.startswith('>'):
            header = re.search(r'>(\S+)(.+)', line)
            idseq = header.group(1)
            if idseq is not records:
                records[idseq]= {'A':0, 'T':0, 'C':0, 'G':0, 'seq':''}
        else:
            # sequence+=line
            records[idseq]['seq']+=line
            A_count=line.count('A')
            records[idseq]['A']+=A_count
            T_count=line.count('T')
            records[idseq]['T']+=T_count
            G_count=line.count('G')
            records[idseq]['G']+=G_count
            C_count=line.count('C')
            records[idseq]['C']+=C_count
    #print(records)
    pprint(records)
                
