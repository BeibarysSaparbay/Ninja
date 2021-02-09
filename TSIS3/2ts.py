a =input().split()
s =[]
for i in a:
    i =int(i)
    if i > 0:
        s.append(i)
print(min(s))
