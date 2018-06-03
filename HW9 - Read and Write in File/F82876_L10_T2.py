import sys

f = open(sys.argv[1])
search = sys.argv[2]

d = {}

for line in f:
	d[line.split(':')[0]] = line.split(':')[1]
print d
for i in d:
	if(d == search):
		print "Found"
		break

f.close()