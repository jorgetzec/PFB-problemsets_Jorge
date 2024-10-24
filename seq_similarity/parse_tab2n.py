#!/usr/bin/env python3

## parse_tab2n.py ss_randall-200_v_qfo_BL50.txt ss_randall-200_v_qfo_BP62.txt ss_randall-200_v_qfo_VT10.txt ...

## read a blast tabular output file with multiple query results 
## and report the median percent identity and alignment length of the top hit for each query

import sys
import statistics

## print out command line 
if (len(sys.argv) < 5):
    print("# " + " ".join(sys.argv))
else:
    print("# " + " ".join(sys.argv[0:5])+' ...')

## blastp -outfmt 7/ ssearch -m8C fields
field_names = ('qseqid','sseqid','percid','alen','mism','gaps','qstart','qend','sstart','send','evalue','bits')

## integer fields
int_fields = ('alen','mism','gaps','qstart','qend','sstart','send')

## floating point fields
flt_fields = ('percid','evalue','bits')


## this version of read_result_file() in parse_tab2.py reads multiple
## results from a file, and returns the first result for each query sequence

def read_nresults_file (result_file):

    results = []

    with open(result_file,'r') as rfd:
        new_result = False
        for line in rfd:
            if line.startswith('# Query:'):
                new_result = True
                continue
            elif line.startswith('#'):
                continue
            
            data = dict(zip(field_names,line.strip('\n').split('\t')))

            for f in int_fields:
                data[f] = int(data[f])

            for f in flt_fields:
                data[f] = float(data[f])

            if (new_result):
                results.append(data)
                new_result=False

    return results

mat_info = {}
mat_names = []

for rfile in sys.argv[1:]:

    ## extract matrix name from 'ss_rand5-200_v_qfo_BL50.txt'

    prefix = rfile.split('.')[0]
    matrix = prefix.split('_')[-1]

    ## read dat

    mat_data = read_nresults_file(rfile)

    if (len(mat_data)>0):
        ## should have multiple results from multiple queries

        alen_list = [x['alen'] for x in mat_data]
        alen_med = statistics.median(alen_list)
        
        percid_list = [x['percid'] for x in mat_data]
        percid_med = statistics.median(percid_list)

        eval_list = [x['evalue'] for x in mat_data]
        eval_med = statistics.median(eval_list)

        mat_info[matrix] = {'alen':alen_med, 'percid':percid_med, 'nsamp':len(percid_list), 'eval':eval_med}
        mat_names.append(matrix)
    else:
        sys.stderr.write("no data from %s\n",rfile)

s_mat_list = ['VT10','VT20','VT40','VT80','VT160','BP62','BL50']
bl_mat_list = ['PAM30','PAM70','BLOSUM80','BLOSUM62']

if (mat_names[0] in s_mat_list):
    disp_mat_list = s_mat_list
else:
    disp_mat_list = bl_mat_list

## print out header for table
print('\t'.join(['matrix','percid','alen','evalue','N']))
for m in disp_mat_list:
    if (m in mat_info):
        print('\t'.join([m,'{:.2f}'.format(mat_info[m]['percid']),'{}'.format(mat_info[m]['alen']),'{:.2g}'.format(mat_info[m]['eval']),'{}'.format(mat_info[m]['nsamp'])]))
