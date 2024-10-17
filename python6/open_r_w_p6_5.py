#!/usr/bin/env python3

# --- Problem 8

# In the bash
# curl -O https://raw.githubusercontent.com/prog4biol/pfb2024/master/files/Python_06.fastq

countLine=0
charactNum=0

with open("Python_06.fastq", "r") as fq_file_obj:
    for line in fq_file_obj:
        line = line.rstrip()
        countLine +=1
        charactNum += len(line)
    averageLine = charactNum/countLine
print(f'REPORT \nTotal number of lines: {countLine} \nTotal number of characters: {charactNum} \nAverage line length: {averageLine}')


