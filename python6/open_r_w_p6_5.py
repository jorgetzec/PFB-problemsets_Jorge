#!/usr/bin/env python3

# --- Problem 9

# In the bash
# curl -O https://github.com/prog4biol/pfb2024/blob/master/files/Python_06.fasta

import sys

records = {}
sequence = ''

with open(sys.argv[1], "r") as fa_file_obj:
    for line in fa_file_obj:
        line = line.rstrip()
        if line.startswith('>'):
            print(line)
            sequence = line[1:]
            records[sequence]= ''
        else:
            records[sequence]=line
print(records)
