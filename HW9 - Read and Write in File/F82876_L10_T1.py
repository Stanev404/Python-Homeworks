import sys
 
f = open(sys.argv[1])
res = open(sys.argv[2],'w')
 
lst=[]
lst=f.readlines()

lst.sort()
for line in lst:
        res.write(line)
 
f.close()
res.close()