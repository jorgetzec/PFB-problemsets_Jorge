#!/usr/bin/env python3

# --- Problem 10

# In the bash
# curl -O https://github.com/prog4biol/pfb2024/blob/master/files/Python_06.fasta

ferret_all_set_g_stableIDv = set('')
count_gID_1=0

with open('ferret_all_genes.tsv', "r") as ferret_all:
    for line in ferret_all:
        line = line.rstrip()
        t_stableID, g_stableIDv, t_stableIDv = line.split('\t')
        ferret_all_set_g_stableIDv.add(g_stableIDv)
        count_gID_1 +=1
    # print(ferret_all_gset_g_stableIDv)
    print(count_gID_1)
    ferret_all_set_g_stableIDv.discard('Gene stable ID version')

count_gID_2=0
ferret_pig_set_g_sIDv = set('')
with open('ferret_pigmentation_genes.tsv', "r") as ferret_pigm:
    for line in ferret_pigm:
        line = line.rstrip()
        t_stableID, g_stableIDv, t_stableIDv = line.split('\t')
        ferret_pig_set_g_sIDv.add(g_stableIDv)
        count_gID_2 +=1
    # print(ferret_pig_set_g_sIDv)
    print(count_gID_2)
    ferret_pig_set_g_sIDv.discard('Gene stable ID version')

count_gID_3=0
ferret_prolif_set_g_sIDv = set('')
with open('ferret_stemcellproliferation_genes.tsv', "r") as ferret_prolif:
    for line in ferret_prolif:
        line = line.rstrip()
        t_stableID, g_stableIDv, t_stableIDv = line.split('\t')
        ferret_prolif_set_g_sIDv.add(g_stableIDv)
        count_gID_3 +=1
    # print(ferret_prolif_set_g_sIDv)
    print(count_gID_3)
    ferret_prolif_set_g_sIDv.discard('Gene stable ID version')

ferret_all_set_g_stableIDv
ferret_pig_set_g_sIDv
ferret_prolif_set_g_sIDv

# all the genes that are not cell proliferation genes.
not_cell_prolif= ferret_all_set_g_stableIDv - ferret_prolif_set_g_sIDv
# print(not_cell_prolif)

# all genes that are both stem cell proliferation genes and pigment
pig_prolif = ferret_pig_set_g_sIDv & ferret_prolif_set_g_sIDv
print(pig_prolif)