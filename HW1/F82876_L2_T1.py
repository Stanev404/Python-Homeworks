import sys

arr = sys.argv[1:]
bool = True
try:
	arr[0] = int(arr[0])
    	for i in range(0, len(arr) - 1):
        	arr[i]=int(arr[i])
        	arr[i+1]=int(arr[i+1])
        	if (arr[i] > arr[i+1]):
        		bool=False
except:
	for j in range(0, len(arr)-1):
        	if (arr[j]>arr[j+1]):
            		bool=False

if (bool == True):
    print "sorted"
else:
    print "unsorted"
