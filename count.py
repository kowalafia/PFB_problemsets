#!/usr/bin/env python3

import sys

count1 = int(sys.argv[1])
count2 = int(sys.argv[2])

range(count1,count2)

print(count1,count2)

for num in range(count1, count2+1):
	print(num)

for num in range(count1, count2+1):
	if num%2==1:
		print(num)

newseq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in newseq:
	print(seq)

newseq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in newseq:
	print(len(seq),seq, sep='\t')

newseq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
position = 0
for seq in newseq:
	position+=1
	print(position, len(seq),seq, sep='\t')


newseq = ('ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC')
for seq in newseq:
	print(len(seq),seq, sep='\t')




