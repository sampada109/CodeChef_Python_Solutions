a = int(input())
b = int(input())
area = a*b 
peri = 2*(a+b)
if area>peri:
    print('Area\n',area)
elif area==peri:
    print('Eq\n',area)
else:
    print('Peri\n',peri)
