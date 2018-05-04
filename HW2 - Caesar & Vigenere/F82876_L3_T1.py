import sys
arr = sys.argv[1:]
result = ""
current = arr[0]
move = int(arr[1])
rem = move % 26
for i in current:
	b = ord(i) + rem
	if(b > ord('Z')):
		 b-=26
	c = str(unichr(b))
	result += c
print result
