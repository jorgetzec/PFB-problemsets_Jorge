#!/usr/bin/env python3


# In the termimal (bash)
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_06.seq.txt


# --- Problem 6
with open("Python_06.txt", "r") as text_file_obj, open("Python_06_uc.txt", "w") as writeText_obj:
    for line in text_file_obj:
        line = line.rstrip()
        writeText_obj.write(f'{line}\n')

