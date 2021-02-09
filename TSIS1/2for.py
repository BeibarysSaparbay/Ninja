a =input()
b =input()
a = int(a)
b = int(b)
c = input()
d = input()
c = int(c)
d = int(d)
for i in range(a,b+1):
    if i%d==c:
        print(i,end=" ")