#!/usr/bin/env python3

import os, sys, re


# PART 1

## begin your code

# seq_list = list()
# count_line = 0

# with open(sys.argv[1], "r") as faq_file_obj:
#     for line in faq_file_obj:
#         line = line.rstrip()
#         count_line+=1
#         if count_line%4 == 2 :
#             seq_list.append(line)

# print(seq_list)

# PART 2

# sequence='ACTGCATCCTGGAAAGAATCAATGGTGGCCGGAAAGTGTTTTTCAAATACAAGAGTGACAATGTGCCCTGTTGTTT'
# kmer_length = 3

# kmers_list = list()
# size = len(sequence)
# for nt in range(size- kmer_length + 1):
#     kmer = sequence[nt: nt + kmer_length]
#     kmers_list.append(kmer)

# print(kmers_list)

# PART 3


# kmer_list = ['ACT', 'CTG', 'TGC', 'GCA','ACT', 'CTG', 'TGC', 'GCA', 'CAT', 'ATC', 'TCC', 'CCT', 'CTG', 'TGG', 'GGA', 'GAA', 'AAA', 'AAG', 'AGA', 'GAA', 'AAT', 'ATC', 'TCA', 'CAA', 'AAT', 'ATG', 'TGG', 'GGT', 'GTG', 'TGG', 'GGC', 'GCC', 'CCG', 'CGG', 'GGA', 'GAA', 'AAA', 'AAG', 'AGT', 'GTG', 'TGT', 'GTT', 'TTT', 'TTT', 'TTT', 'TTC', 'TCA', 'CAA', 'AAA', 'AAT', 'ATA', 'TAC', 'ACA', 'CAA', 'AAG', 'AGA', 'GAG', 'AGT', 'GTG', 'TGA', 'GAC', 'ACA', 'CAA', 'AAT', 'ATG', 'TGT', 'GTG', 'TGC', 'GCC', 'CCC', 'CCT', 'CTG', 'TGT', 'GTT', 'TTG', 'TGT', 'GTT', 'TTT']
# kmer_count_dict = dict()
# count= 0

# for kmer in kmer_list:
#     if kmer in kmer_count_dict:
#         kmer_count_dict[kmer] += 1
#     else:
#         kmer_count_dict[kmer] = 1

# kmer_count_dict = dict(sorted(kmer_count_dict.items(),reverse= True, key=lambda item: item[1]))
# print(kmer_count_dict)