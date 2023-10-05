t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    run = 0
    count = 0
    for i in range(n):
        run = l[i] + run
        s = (run/(i+1))*100
        if s==100:
            count +=1 
    print(count)        
