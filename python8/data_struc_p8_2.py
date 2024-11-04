#!/usr/bin/env python3

# in bash terminal
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_08.fasta

# Problem 1

import sys
import re
from collections import Counter
from pprint import pprint
from Bio.Seq import Seq
records = {}


with open(sys.argv[1], 'r') as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        if line.startswith('>'):
            header = re.search(r'>(\S+)(.+)', line)
            idseq = header.group(1)
            if idseq is not records:
                records[idseq]= {'seq':'','frame1':[], 'frame2':[],'frame3':[]}
        else:
            records[idseq]['seq']+=line
        sequence = records[idseq]['seq']
        for codon in re.findall(r'(.{3})', sequence):
            records[idseq]['frame1'].append(codon)
                        #pprint(codon)
        sequence_f2= sequence[1:]
        for codon in re.findall(r'(.{3})', sequence_f2):
            records[idseq]['frame2'].append(codon)
                        #pprint(codon)
        sequence_f3= sequence[2:]
        for codon in re.findall(r'(.{3})', sequence_f3):
            records[idseq]['frame3'].append(codon)
                        #pprint(codon)
pprint(records)
print ()


#for seq in records[idseq][seq]:
# for sequenes in records[idseq]['seq']:
#     print(Seq(sequenes))
