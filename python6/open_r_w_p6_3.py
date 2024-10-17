#!/usr/bin/env python3

# --- Problem 7
with open("Python_06.seq.txt", "r") as text_file_obj:
    for line in text_file_obj:
        line = line.rstrip()
        gene_id, seq = line.split('\t')
        complement=''
        for base in seq:
          if base=='T':
            complement+='A'
          elif base=='A':
            complement+='T'
          elif base=='C':
            complement+='G'
          elif base== 'G':
            complement+='C'
        rev_complement=complement[::-1]
        print(f'>{gene_id} \n{rev_complement}')

# in the terminal
#  ./open_r_w_p6_3.py > Python_06_rev_comp.seq.fa # This is to creat a new fasta file redirecting the output. 



