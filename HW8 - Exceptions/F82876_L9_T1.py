import math

def f(x):
	return x*x*x+3*x-5

def bisection(a,b, func):
	try:
		a= int(a)
		b= int(b)
		if(f(a)*f(b) > 0):
			raise Exception
		
		c=(a+b)/2.0

		while((b-a)/2.0 >= 0.001 or f(c) != 0):
			c=(a+b)/2.0
			if(f(c) == 0.0):
				return c
			
			elif(f(c)*f(a) < 0.0):
				b = c
			elif(f(c)*f(b) < 0.0):
				a = c
	except Exception:
		raise Exception("Negative number used")
	except ValueError:
		raise ValueError("Value error")
	
