#!/usr/bin/env python3

# --- Problem 3

# In the bash
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_07.fasta
import re


# with open('Python_07.fasta', "r") as fasta_file:
#     for line in fasta_file:
#         line = line.rstrip()
#         header_fa = re.search(r'^>\S+\s*.*', line)
#         if header_fa:
#             print(header_fa)
 
with open('Python_07.fasta', "r") as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        header_fa = re.match(r'^>\S+\s*.*', line)
        if header_fa:
            print(header_fa)






