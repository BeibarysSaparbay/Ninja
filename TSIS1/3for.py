a = input()
a = int(a)
b = input()
b = int(b)
for i in range(a , b + 1 ):
    if (i**(1/2)) % 2 == 0 or (i**(1/2)) % 2 == 1:
        print(i,end=" ")
    else:
        continue