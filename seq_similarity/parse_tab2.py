
#!/usr/bin/env python3

import sys

if (len(sys.argv) < 5):
    print("# " + " ".join(sys.argv))
else:
    print("# " + " ".join(sys.argv[0:5])+' ...')


field_names = ('qseqid','sseqid','percid','alen','mism','gaps','qstart','qend','sstart','send','evalue','bits')

int_fields = ('alen','mism','gaps','qstart','qend','sstart','send')
flt_fields = ('percid','evalue','bits')


def read_result_file (result_file):

    results = []

    with open(result_file,'r') as rfd:
        for line in rfd:
            if line.startswith('#'):
                continue
            
            data = dict(zip(field_names,line.strip('\n').split('\t')))

            for f in int_fields:
                data[f] = int(data[f])

            for f in flt_fields:
                data[f] = float(data[f])

            results.append(data)

    return results

mat_info = {}
mat_names = []

for rfile in sys.argv[1:]:

    ## extract matrix name from 'ss_rand5-200_v_qfo_BL50.txt'

    prefix = rfile.split('.')[0]
    matrix = prefix.split('_')[-1]

    ## read dat

    mat_data = read_result_file(rfile)

    if (len(mat_data)>0):
        mat_info[matrix] = {'alen':mat_data[0]['alen'], 'percid':mat_data[0]['percid']}
        mat_names.append(matrix)
    else:
        sys.stderr.write("no data from %s\n",rfile)


s_mat_list = ['VT10','VT20','VT40','VT80','VT160','BP62','BL50']


for m in s_mat_list:
    if (m in mat_info):
        print('\t'.join([m,str(mat_info[m]['percid']),str(mat_info[m]['alen'])]))