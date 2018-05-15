import sys

f = open(sys.argv[1])
search = sys.argv[2]

d = {}

for line in f:
	x = line.split(":")
	a = x[0]
	b = x[1]
	c = len(b)-1
	b = b[0:c]

	d[a] = b

for i in d:
	
	if(d[i] == search):
		print i
		break

f.close()
