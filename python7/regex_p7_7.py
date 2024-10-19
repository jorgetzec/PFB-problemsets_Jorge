#!/usr/bin/env python3


# In the bash
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_07_ApoI.fasta
import re

# --- Problem 7
#R = A or G 
#Y = C or T


with open('Python_07_ApoI.fasta', "r") as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        for cut_site in re.finditer(r'([AG])AATT([CT])', line):
            #print(cut_site)
            before=cut_site.group(1)
            after=cut_site.group(2)
            newline = re.sub(r'([AG])AATT([CT])',r'\1^AATT\2', line)
            print(newline)




# with open('Python_07_ApoI.fasta', "r") as fasta_file:
#     for line in fasta_file:
#         line = line.rstrip()
#         cut_site = re.search(r'(A|G)AATT(C|T)', line)
#         print(cut_site)


# --- Problem 8
fragments = []
with open('Python_07_ApoI.fasta', "r") as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        for cut_site in re.finditer(r'([AG])AATT([CT])', line):
            #print(cut_site)
            before=cut_site.group(1)
            after=cut_site.group(2)
            newline = re.sub(r'([AG])AATT([CT])',r'\1^AATT\2', line)
            fragments+=newline.split('^')
print(fragments)
print(sorted(fragments, key=len))


# Creating an empty dictonary
len_segmets = {}

# builting the dictionary
for frag in fragments:
    len_segmets[len(frag)]= frag
   
#print(len_segmets)




