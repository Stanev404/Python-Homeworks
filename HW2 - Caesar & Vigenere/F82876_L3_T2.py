import collections
import sys
def Ceaser(text,key):
	result= ""
	rem = key % 26
	for i in text:
		b = ord(i) + rem
		if(b > ord('Z')):
			b-=26
		c = str(chr(b))
		result +=c
	return result



text = sys.argv[1]
key = sys.argv[2]

result = ""
index = 0
for i in text:
	numericKey= key[index]
	left_key = ord(numericKey)
	right_key = ord("A")
	final_key = left_key - right_key
	result += Ceaser(i,final_key)
	index += 1
	if (index == len(key)):
		index = 0
print result
		
