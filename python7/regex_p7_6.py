#!/usr/bin/env python3


# In the bash
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_07_ApoI.fasta
import re

# --- Problem 6
#The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotides. See the IUPAC table to identify the nucleotide possibilities for the R and Y. Write a regular expression to find and print all occurrences of the site in the following sequence Python_07_ApoI.fasta.

# This runs well but the printing section look ugly
# with open('Python_07_ApoI.fasta', "r") as fasta_file:
#     for line in fasta_file:
#         line = line.rstrip()
#         cut_site = re.findall(r'[(A)(G)]AATT[(C)(T)]', line)
#         print(cut_site)


with open('Python_07_ApoI.fasta', "r") as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        for cut_site in re.findall(r'[(A)(G)]AATT[(C)(T)]', line):
            print(cut_site)


#R = A or G 
#Y = C or T





