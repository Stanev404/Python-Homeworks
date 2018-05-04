import sys
sz = len(sys.argv)

res = {}
for i in range(1,sz,1):
	text = sys.argv[i]

	for i in text:
		if(res.has_key(i) == True):
			res[i] +=1
			#increase the value of this key
		else:
			#insert in res with value of 1
			res[i] = 1
print res
