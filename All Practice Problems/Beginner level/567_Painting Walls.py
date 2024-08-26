# cook your dish here

n = int(input())

for i in range(n):
    
    l, b, m = map(int, input().split())
    
    area = l*b
    cost_area = 2 * area 
    
    wall = m // cost_area
    
    print(wall)
