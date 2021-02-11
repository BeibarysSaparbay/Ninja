x = lambda a: a + 10
print(x(5))

s =lambda a ,b : a*b
print(s(3,4))

def myfunc(n):
	return lambda a: a * n
   	
l = myfunc(2)
print(l(3))

t =myfunc(3)
print(t(30))