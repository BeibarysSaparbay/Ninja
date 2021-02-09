a =int(input())
s = dict()
for i in range(0,a):
    x,y=input().split()
    s[x]=y
    s[y]=x
l =input()
r = s.get(l) 
print(r)