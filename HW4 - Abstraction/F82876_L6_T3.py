import sys
def magic(num,arr,first,last):
        if((first+1==last) and (arr[first] != num)):
                return "not found"
        else:
                if(num == arr[(last + first)/2]):
                        return (last+first)/2 # sporno + 1
                elif(num < arr[(last+first)/2]):
                        return magic(num,arr,first,(last+first)/2)
                else:
                        return magic(num,arr,(last+first)/2,last)
 
 
 
number = int(sys.argv[1])

arr = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272, 288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444, 486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898, 900, 903, 908, 909, 959, 988] 
size = len(arr)
 
res = magic(number,arr,0,size)
if(res == "not found"):
        print "not found"
else:
        print "found at",res
