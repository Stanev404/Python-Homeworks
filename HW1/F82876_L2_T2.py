import sys
arr = sys.argv[1:]
first=arr[0]
second=arr[1]
first = first.replace(" ","")
second = second.replace(" ","")
first = first.lower()
second = second.lower()

first_res = []
second_res = []


for i in range(0,len(first)):
	first_res.append(first[i])
for j in range(0,len(second)):
	second_res.append(second[j])

if(len(first_res) == len(second_res)):
	for i in first_res:
		if i in second_res:
			second_res.remove(i)
	if(len(second_res) == 0):
		print "True"
	else:
		print "False"
else:
	print "False"						
