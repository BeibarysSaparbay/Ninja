a = input().split()
cnt = 0
s = []
for i in a:
    if i == '0':
        cnt += 1
    else:
        s.append(i)
r = 0
while cnt != r:
    s.append('0')
    r += 1