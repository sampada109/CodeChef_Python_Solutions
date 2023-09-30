t = int(input())
for i in range(t):
    dr,pr,dp,pp = map(int,input().split())
    d = dp/dr 
    p = pp/pr 
    if d<p:
        print(-1)
    elif d==p:
        print(0)
    else:
        print(1)
