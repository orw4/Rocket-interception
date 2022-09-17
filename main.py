# A program that shows how rockets can be intercepted
# 12/07/2022

#TODO
#find 3 points-
#find equation in x
#find equation in y
#find the time when the rocket passes 3/4 of the route (or something else)
#find inceptors equations in x
#find inceptors equation in y
#find velocity and angle
#find routes

# Finds the coordinations of the rocket
# Gets the distance of the rocket and the angle where the rocket can be found
# Returns a coordinate (x,y)
def coordinations(distance, angle):
    x = distance * math.cos(angle)
    y = distance * math.sin(angle)
    return [x,y]

# Finds the x equation and the y equation of a rocket
# Gets the x/y values of 3 points and the frequency of the rocket coordinations' checking
# Returns the velocity in the first point (t = 0) and the acceleration of the rocket in x/y
def routeEquation(p1, p2, p3, frequency):
    mat = [[frequency, 0.5 * frequency ** 2, p2 - p1], [2 * frequency, 2 * frequency ** 2, p3 - p1]]
    [v, a] = solve(mat)
    return [v, a]

# Finds the route of the rocket
# Gets a list of 3 points (x,y)
# Returns (a,b,c) such that the route of the rocket is ax^2+bx+c
def route(points):
    mat = [0,0,0]
    for i in range(3):
        mat[i] = [(points[i][0]) ** 2, points[i][0], 1, points[i][1]]
    [a, b, c, d] = solve(mat)
    return [a,b,c]

# Finds the time when the rocket passes a certain percent of its route. If it have passed it, return half the time left
# Gets the rocket's route and a percent
# Returns the time when the rocket passes this percent of its route (for exemple 50% - half the route). If the rocket
# have already passed it, returns half of the time until it gets to the ground
def when(route, percent):
    return 0

# Solves an equation system (as a matrix)
# Gets the matrix
# Returns the equations system's solution
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

# Finds the right route to intercept the rocket
# Gets the route of the rocket as (a,b,c) when the route is ax^2+bx+c and the frequency of the
# coordination checkings (how many time passed between each point of the rocket)
# Returns the velocity and angle which would intercept the rocket
def intercept(route, frequency):
    angle = route
    velocity = route
    return[velocity, angle]

# Sets a value using input
def set(val):
    print("What is", val, "?")
    ans = input(" ")
    return float(ans)




import math
points = [0,0,0]
for i in range(3):
    print("point", i+1)
    d = set("the distance from the rocket")
    a = set("the angle you see the rocket")
    points[i] = coordinations(d, a)
[a,b,c] = route(points)