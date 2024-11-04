#!/usr/bin/env python3

''' 
For comand line

for m in BL50 BP62 VT10 VT160 VT20 VT40 VT80; do 

curl -O https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-200_v_qfo_${m}.txt

done


---
Usage of this script
./parse_tab.py ss_rand5-*.txt
./parse_tab.py ss_rand5-200_*.txt

'''


import sys

hit_files = []

field_str = "q_seqid s_seqid percid alen mism gaps q_start q_end s_start s_end evalue bits"
fields=field_str.split(' ')

hits_list = []

for hit_file in sys.argv[1:]:

    with open(hit_file,'r') as fin:
        for line in fin:
            if line[0]=='#':
                continue
            hit_data = dict(zip(fields,line.strip('\n').split('\t')))
            hit_data['file'] = hit_file
            hits_list.append(hit_data)
            break

for hit in hits_list:
    print('\t'.join([hit[x] for x in ('file','percid','alen','evalue')]))