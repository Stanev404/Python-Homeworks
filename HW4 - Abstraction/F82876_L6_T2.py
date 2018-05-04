import sys
 
 
def digame_stepen(num,stepen):
        if(stepen == 0):
                return 1
        else:
                return num * digame_stepen(num,stepen - 1)
 
 
 
 
 
num = int(sys.argv[1])
stepen = int(sys.argv[2])
print digame_stepen(num,stepen)

