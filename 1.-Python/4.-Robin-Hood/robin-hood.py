# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 12:29:29 2020

@author: Cinthya Blois
"""

#quadrants = Q1, Q2, Q3, Q4
#Q1: x > 0 and y > 0
#Q2: x < 0 and y > 0
#Q3: x < 0 and y < 0
#Q4: x > 0 and y < 0

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

coordinates_x = map(lambda x: x[0], points)
coordinates_x = list(coordinates_x)
coordinates_y = map(lambda x: x[1], points)
coordinates_y = list(coordinates_y)

#print(coordinates_x)
#print(len(coordinates_x))
#print(coordinates_y)
#print(len(coordinates_y))

res = list(set(points))
print("Total duplicates:",len(points)-len(res))

coordinates_duplicate = list(set([i for i in points
                            if points.count(i) > 1]))

print("This are the coordinates that Robin Hood hit more than one arrow:",coordinates_duplicate)

#res = list(set([ele for ele in points 
#            if points.count(ele) > 1])) 

#print(res)

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

for i in range(0,len(points)):
    x = coordinates_x[i]
    y = coordinates_y[i]
    if (x > 0) & (y > 0):
        Q1+=1
    elif (x < 0) & (y > 0):
        Q2+=1
    elif (x < 0) & (y < 0):
        Q3+=1
#    elif (x > 0) & (y < 0):
#        Q4+=1
    else:
        Q4+=1
#        print("An arrow hits the center")

print("Number of arrows in Q1, Q2, Q3 and Q4 is",Q1,",", Q2,",", Q3,"and",Q4,", respectively.")
#print(Q1+Q2+Q3+Q4)

# The distance (d) can be define: d = sqrt(x^2 + y^2)

def distance(dist):
    #for i in range(0,len(points)):
        x = coordinates_x[dist]
        y = coordinates_y[dist]
        import math
        return math.sqrt(x**2 + y**2)

d_point = []

for i in range(0,len(points)):
    d = distance(i)
    d_point.append(d)

min_d_point = d_point.index(min(d_point))
print("The point closest to the center is:",points[min_d_point],"with distance:",d_point[min_d_point])

radius = 9
d_circ = 0
d_circ_out = 0

for i in range(0,len(points)):
    if distance(i) <= radius:
        d_circ +=1
    else:
        d_circ_out +=1

print("For this radius,",d_circ_out,"arrows don't hit the target.")
print("For this radius,",d_circ,"arrows do hit the target.")