#!/usr/bin/env python3

# --- Problem 1

# In the bash
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_07_nobody.txt
import re

with open('Python_07_nobody.txt', "r") as text_file:
    for line in text_file:
        line = line.rstrip()
        print(re.search(r'Nobody', line))
