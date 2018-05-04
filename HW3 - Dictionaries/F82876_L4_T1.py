import sys
inp = sys.argv[1]
res = []
d = {1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'}
for i in d:
	if(inp == d[i]):
		res.append(i)

print res
