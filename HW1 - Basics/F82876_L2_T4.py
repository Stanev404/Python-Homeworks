import sys
from pprint import pprint
arr = sys.argv[1:]

res = []
res.append(int(arr[0])) 

for i in range(1,len(arr)):
	flag= False
	for j in range(0,len(res)):
		if(int(arr[i]) == int(res[j])):
			flag = True
			break
	if(flag == False):
		res.append(int(arr[i]))

for i in range(0,len(res)):
	for j in range(i+1,len(res)):
		if(res[i] > res[j]):
			temp = res[i]
			res[i] = res[j]
			res[j] = temp

pprint(res)
#print '[',
#for i in range(0,len(res)):
#	print res[i],

#print "]"
