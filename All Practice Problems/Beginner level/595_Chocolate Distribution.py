# cook your dish here

t = int(input())

for i in range(t):
    
    n = int(input())
    
    if n%2 == 0:
        mini = n//2
    else:
        mini = (n//2) + 1 
    
    maxi = n 
    
    print(mini, maxi)
