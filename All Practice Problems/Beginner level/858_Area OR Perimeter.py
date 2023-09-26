a = int(input())
b = int(input())
area = a*b 
peri = 2*(a+b)
if area>peri:
    print('Area')
elif area==peri:
    print('Equal')
else:
    print('Peri')
