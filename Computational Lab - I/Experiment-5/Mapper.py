#!/usr/bin/env python
import sys
m_r=2
m_c=3
n_r=3
n_c=2
i=0
for line in sys.stdin:
	el=map(int,line.split())
	if(i<m_r):
		for j in range(len(el)):
			for k in range(n_c):
				print('%d\t%d\t%d\t%d' %(i,k,j,el[j]))
	else:
		for j in range(len(el)):
			for k in range(m_r):
				print('%d\t%d\t%d\t%d' %(k,j,i+m_r,el[j]))
	i=i+1
