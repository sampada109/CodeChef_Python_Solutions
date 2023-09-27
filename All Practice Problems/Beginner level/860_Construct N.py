t = int(input())
for i in range(t):
    n = int(input())
    if n%2==0 or n%7==0 :
        print('YES')
    elif n>7:
        print('YES')
    else:
        print('NO')
