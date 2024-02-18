# cook your dish here
t = int(input())

for i in range(t):
    l = list(map(int,input().split()))
    
    c = l.count(1)
    
    if(c>=4):
        print("YES")
    else:
        print("NO")
