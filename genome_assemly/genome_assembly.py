#!/usr/bin/env python3

import sys
import re
from pprint import pprint

contig_dic = {}
contig_num = 0



with open(sys.argv[1], "r") as fa_file_obj:
    for line in fa_file_obj:
        line = line.rstrip()
        if line.startswith('>'):
            id_contig = re.search(r'(ti.\d{8})', line)
            id_contig = id_contig.group(1)
            contig_dic[id_contig] ={'len':0, 'Seq':''}
            lenght_contig = re.search(r'len=(\d+)', line)
            lenght_contig= lenght_contig.group(1)
            contig_dic[id_contig]['len']=int(lenght_contig)
            contig_num += 1
        else:
            contig_dic[id_contig]['Seq'] += line




sorted_contig_dic = dict(sorted(contig_dic.items(), reverse=True, key=lambda item: item[1]["len"]))
#print(sorted_contig_dic)

longest_contig= list(sorted_contig_dic.keys())[0]
shortest_contig= list(sorted_contig_dic.keys())[-1]
print(f'The shortest contig is {longest_contig}')
print(f'The shortest contig is {shortest_contig}')

## ----To test if is working the sorting
#Total lenght

lenght=[]
for id_contig in contig_dic:
    lenght.append(contig_dic[id_contig]['len'])

sorted_lengt_contig= sorted(lenght)
print(f'The lenghts of the sorted lenghts are: {sorted_lengt_contig}')

total_lenght =  sum(lenght)
print(f'The total lenght is {total_lenght}')


lenght_for_N50_L50= 0
half_contig_lenght = (total_lenght//2)
print(half_contig_lenght) 
print('\n')

contigs_for_N50_L50=[]
for id_contig in sorted_contig_dic:
    lenght_for_N50_L50 += sorted_contig_dic[id_contig]['len']
    print(f'total is: {lenght_for_N50_L50}')
    if lenght_for_N50_L50 > half_contig_lenght:
        print(sorted_contig_dic[id_contig]['len'])
        break

#print(lenght_for_N50_L50)
