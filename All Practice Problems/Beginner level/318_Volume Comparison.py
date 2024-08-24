# cook your dish here

l , w, h , s = map(int, input().split())

cbd = l*w*h 

cb = s**3

if( cbd > cb ):
    print("Cuboid")
elif( cbd == cb ):
    print("Equal")
else:
    print("Cube")
