#!/usr/bin/env python3

# In the termimal (bash)
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_06.txt

# --- Problem 5
with open("Python_06.txt", "r") as text_file_obj:
    for line in text_file_obj:
        line = line.rstrip()
        print(line)

