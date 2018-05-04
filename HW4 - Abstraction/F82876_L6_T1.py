import sys
def fib(num):
        if (num <= 1):
                return num
        else:
                return fib(num-1) + fib(num - 2)
def fibs(i,num):
        arr = []
        i=i-1
        while(i < num):
                arr.append(fib(i))
                i +=1
        return arr
start = int(sys.argv[1])
final = int(sys.argv[2])
print fibs(start,final)
