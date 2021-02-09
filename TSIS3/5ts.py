a =input().split()
k = int(input())
if k > 0:
    for i in range(k-1,len(a)):
        print(a[i],end=" ")
    for i in range(0,k-1):
        print(a[i],end=" ")
else:
    for i in range(k-1,len(a)):
        print(a[i],end=" ")
    for i in range(0,k-1):
        print(a[i],end=" ")
