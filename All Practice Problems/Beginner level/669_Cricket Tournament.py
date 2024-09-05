# cook your dish here

t = int(input())

for i in range(t):
    
    teams , matches = map(int, input().split())
    
    if( teams > matches ):
        print("YES")
    else:
        print("NO")
