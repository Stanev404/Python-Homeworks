import sys
arr = sys.argv[1:]
flag=False
for i in range(0,len(arr)):
	for j in range(i+1,len(arr)):
		if(arr[i] == arr[j]):
			print "True"
			flag=True
			break
	if(flag==True):
		 break
if(flag==False):
	print "False"
