#!/usr/bin/env python3

# Problem 1


''''
Create a function to format a string of DNA so that each line is no more than 60 nt long. 
Your function will:
INPUT: a string of DNA without newlines
OUTPUT: a string of DNA with lines no more than 60 nucleoties lon

'''

from Bio import SeqIO
import sys

fasta = sys.argv[1]

with open(fasta, "r") as fasta_file:
    for seq_record in SeqIO.parse(fasta_file, 'fasta'):
        print(seq_record.name)
        print(seq_record.seq)

        
''''
In the termila:
./biopy_1.py ../python8/Python_08.fasta
'''