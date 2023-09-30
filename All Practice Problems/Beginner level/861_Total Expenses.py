t = int(input())
for i in range(t):
    q,p = map(int,input().split())
    if q>1000:
        d = (q*p) * 0.1            #discount
        print((q*p)-d)             # total - discount
    else:
        print(q*p)
