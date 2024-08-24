# cook your dish here

p , n = map(int, input().split())

if( p < n ):
    print("INCREASED")
elif( p == n ):
    print("SAME")
else:
    print("DECREASED")
