t = int(input())
for i in range(t):
    z,y,a,b,c = map(int,input().split())
    r = z-y
    k = a+b+c 
    if r>=k:
        print('YES')
    else:
        print('NO')
