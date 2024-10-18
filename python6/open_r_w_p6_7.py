#!/usr/bin/env python3

# --- Problem Extra!!!!

# In the bash
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_06.seq.txt

genes = {}
nt_count = {}
with open('Python_06.seq.txt', "r") as sequence_file:
    for line in sequence_file:
        line = line.rstrip()
        gene_ID, seq = line.split('\t')
        genes[gene_ID]=seq
        # print(genes)
        for nt in seq:
            if gene_ID in genes:     
                genes[nt]+=1
            else:
                nt_count[nt] = 1



        #     if nt in nt_count:
        #         nt_count[nt] += 1
        #     else:
        #         nt_count[nt] = 1
        #     print(nt_count)