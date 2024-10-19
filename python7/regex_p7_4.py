#!/usr/bin/env python3


# In the bash
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_07.fasta
import re

# --- Problem 4

# To test the regex synthaxis: https://regex101.com/

with open('Python_07.fasta', "r") as fasta_file:
    for line in fasta_file:
        line = line.rstrip()
        if line.startswith('>'):
            header_fa = re.search(r'>(\S+)(.+)', line)
            idname = header_fa.group(1)
            descpname = header_fa.group(2)
            print('id:', idname)
            print('desc:', descpname)







