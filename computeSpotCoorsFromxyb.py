import sys
#10100317_v0.asc Z+F 0.0 0.0 1.5 0.036 0 180 0 360
#10100317_v1.asc Z+F 15.00000 0 1.5 0.036 0 180 0 360
#10100317_v2.asc Z+F 0 15.00000 1.5 0.036 0 180 0 360
#10100317_v3.asc Z+F -15.00000 0 1.5 0.036 0 180 0 360
#10100317_v4.asc Z+F 0 -15.00000 1.5 0.036 0 180 0 360
#scan 1

scan1 = sys.argv[1]
scan2 = sys.argv[2]
str1 = 
x = [None]*5
y = [None]*5
z = [None]*5
x[0] = 0.0
y[0] = 0.0
z[0] = 1.5 

x[1] = 15.00000
y[1] = 0
z[1] = 1.5 

x[2] = 0
y[2] = 15.00000
z[2] = 1.5 

x[3] = -15.00000
y[3] = 0
z[3] = 1.5 

x[4] = 0
y[4] = -15.00000
z[4] = 1.5 


spot = int(sys.argv[1])

print (x[0] + x[spot])/2, (y[0] + y[spot])/2
