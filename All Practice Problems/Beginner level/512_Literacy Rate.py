# cook your dish here
t = int(input())

for i in range(t):
    p,l = map(float ,input().split())
    
    if((l/p)>=0.75):
        print("YES")
    else:
        print("NO")
