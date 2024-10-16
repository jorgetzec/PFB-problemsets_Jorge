#!/usr/bin/env python3

import sys
DNA=sys.argv[1]

# --- ITEM 6. Counting characters from a string

# DNA='GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG'

DNA_uppercase=DNA.upper()

freqA=DNA_uppercase.count('A')
freqT=DNA_uppercase.count('T')
freqC=DNA_uppercase.count('C')
freqG=DNA_uppercase.count('G')

print(f'The frequency of A is {freqA}, for T is {freqT}, for C is {freqC}, and for G is {freqG}')


# -----ITEM 7. Replace

RNA=DNA.replace('T','U')
print(f'The T in the sequence {DNA} was replaced with U and now looks like {RNA}')

# ---- ITEM 8. Find and replace
RNA2=DNA.replace('T','U').replace('t', 'u')

print(f'The T or t in the sequence {DNA} was replaced with U or u  and now looks like {RNA2}')

# ----ITEM 9. AT content calculation
DNA=DNA.upper()

Acount=DNA.count('A')
Tcount=DNA.count('T')

Ccount=DNA.count('C')
Gcount=DNA.count('G')

TAsprop=(((Acount+Tcount)/len(DNA))*100)
GCsprop=(((Gcount+Ccount)/len(DNA))*100)

print(f'The secuence lenght is {len(DNA)} and the frecuency of Ts is {Tcount} while the frecuency for As is {Acount}. Then, the TA proporcion is {TAsprop}, while the GC proportion is {GCsprop}')


# --- ITEM10. Substring

print(f'The lenght of the substring is {len(DNA[99:200])}')
 
DNA_substring=DNA[99:200]
print(f'The sequences of the DNA subtring is {DNA_substring}')

# --- ITEM11. Counting in the substring

print(f'The number of Gs in the substring is {DNA_substring.count('G')}')

# --- ITEM12. Counting regardless the case (A or a..)

	# This is completed due to the reasigmennt of DNA as uppercase


