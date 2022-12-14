# A program that shows how rockets can be intercepted
# 12/07/2022

import math
prepareTime = 2

# Sets a value using input
def set(val):
    print("What is", val, "?")
    ans = input(" ")
    return float(ans)

# Gets the distance of the rocket and the angle where the rocket can be found and returns a coordinate (x,y)
def coordinations(distance, angle):
    angle = angle * math.pi / 180 # degrees to radians
    x = distance * math.cos(angle)
    y = distance * math.sin(angle)
    return [x,y]

# Returns an array of the times and x,y coordinations of the points
def findPoints():
    points = [[],[],[]]
    for i in range(3):
        print("point", i + 1)
        distance = set("the distance from the rocket")
        angle = set("the angle between the rocket, you and the ground")
        time = (-1) * float(input("How many time in seconds have passed since it checked the distance? "))
        points[i] = coordinations(distance, angle)
        points[i].append(time)
    return points

# Solves an equation system (as a matrix)
def solve(mat):
    for i in range(len(mat)): #number of rows
        for k in range(len(mat)):  # the rows under i
            divide = mat[i][i]
            ki = mat[k][i]
            for j in range(len(mat[i])): #number of columns
                mat[i][j] = mat[i][j] / divide
                if k != i:
                    mat[k][j] = mat[k][j] - mat[i][j] * ki
    for i in range(len(mat)): #moving the answers to the first row
        mat[0][i] = mat[i][len(mat[0]) - 1]
    return mat[0]

# Finds the x,y coordinations of the next point where the rocket will be in 2 seconds, returns the acceleration in x and y and the coordinations of the next point
def nextPoint(points):
    t1 = points[0][2]
    t2 = points[1][2]
    t3 = points[2][2]
    next = []
    returns = []
    for i in range(2): # for x and then for y
        equations = [[t2 - t1, (t2 - t1) ** 2 / 2, points[1][i] - points[0][i]], [t3 - t1, (t3 - t1) ** 2 / 2, points[2][i] - points[0][i]]]
        [v, a, more] = solve(equations)
        returns.append(a)
        point = points[0][i] + v * (prepareTime - t1) + a * (prepareTime - t1) ** 2 / 2
        next.append(point)
    returns.append(next)
    return returns

# Finds the velocity and angle for intercepting the rocket in a given point
def intercept(returns):
    next = returns[2]
    velocities = []
    for i in range(2): # for x and y
        v = next[i] / prepareTime - returns[i] * prepareTime / 2
        velocities.append(v)
    velocity = math.sqrt((velocities[0]) ** 2 + (velocities[1]) ** 2)
    angle = math.atan(velocities[1] / velocities[0]) * 180 / math.pi
    return [velocity, angle]

points = findPoints()
next = nextPoint(points)
ans = intercept(next)
print("v = ", ans[0],", angle = ", ans[1])
