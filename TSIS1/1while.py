a = int(input())
ok  = False 
i = 1
while ok != True:
    if i**2 <= a:
        print(i**2 ,end=" ")
        i += 1
    else:
        ok = True