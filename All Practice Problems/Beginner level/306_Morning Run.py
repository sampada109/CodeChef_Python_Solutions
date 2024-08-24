# cook your dish here

w,h = map(int, input().split())

tt = (2*w) + (2*h)

if ( tt >= 1000 ):
    print("YES")
else:
    print("NO")
