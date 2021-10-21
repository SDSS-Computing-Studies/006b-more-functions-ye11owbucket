#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is scalene
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 1  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
def triangle(a,b,c):
    side=[a,b,c]
    side.sort()
    if side[0]+side[1] < side[2]:
        return 0
    if side[0]**2+side[1]**2 > side[2]**2:
        return 1
    if side[0]**2+side[1]**2 == side[2]**2:
        return 2
    if side[0]**2+side[1]**2 < side[2]**2:
        return 3
    pass