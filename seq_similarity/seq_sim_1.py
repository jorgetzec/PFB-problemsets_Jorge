#!/usr/bin/env python3

''' 
For comand line

for m in BL50 BP62 VT10 VT160 VT20 VT40 VT80; do 

curl -O https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-200_v_qfo_${m}.txt

done

'''
import sys
import re

list_matrix = ['BL50', 'BP62', 'VT10', 'VT160', 'VT20', 'VT40',  'VT80']

name_file =[]
for


with open(sys.argv[1], 'r') as blast_rep:
    for line in blast_rep:
        line = line.rstrip()
        if line.startswith('#'):
            for mtx in list_matrix:
                if mtx in line:
                    print(mtx)




