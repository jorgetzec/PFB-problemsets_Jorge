#!/usr/bin/env python3
'''''
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
    print(hit_file)