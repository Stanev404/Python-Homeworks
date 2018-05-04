
import sys

def reverse_word(given_word):
	if (given_word == ""):
		return given_word
	else:
		return reverse_word(given_word[1:]) + given_word[0]


word = sys.argv[1]
	
reversed = reverse_word(word)

if(word == reversed):
	print True
else:
	print False
