import turtle
import math

class Body:
    def __init__(self, mass, px, py, vx, vy):
        self.mass = mass
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy



G = 6.674*pow(10, -11)
dt = float(pow(10, -7))



def Gravitational_Force(m1, m2, r):           #defining newtonian gravitational force
    F = (G * m1 * m2) / pow(r, 2)
    return(F)



def Motion(px, py, vx, vy, ax, ay):
    px = px + (vx*dt) + (0.5*ax*pow(dt, 2))
    py = py + (vy*dt) + (0.5*ay*pow(dt, 2))
    vx = vx + (ax*dt)
    vy = vy + (ay*dt)
    return(px, py, vx, vy)



def Trajectory(name, x, y, color, dot_size = 1):
    name.shapesize(dot_size)
    name.color(color)
    name.penup()
    name.goto(x, y)
    name.dot(5, color)



def Distance(px1, px2, py1, py2):
    d = math.sqrt(pow(px1 - px2, 2) + pow(py1 - py2, 2))
    return(d)



#Initialising system
b1 = Body(5.97219*pow(10, 24), 0, 5, 0, 0)
b2 = Body(5.97219*pow(10, 24), 4.3301, -2.5, 0, 0)
b3 = Body(5.97219*pow(10, 24), -4.3301, -2.5, 0, 0)

turtle.bgcolor("black")
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle1.shape("circle")
turtle2.shape("circle")
turtle3.shape("circleg")



#Simulation
for i in range(100):
    d12 = Distance(b1.px, b2.px, b1.py, b2.py)
    d23 = Distance(b2.px, b3.px, b2.py, b3.py)
    d13 = Distance(b1.px, b3.px, b1.py, b3.py)

    f12 = Gravitational_Force(b1.mass, b2.mass, d12)
    f23 = Gravitational_Force(b2.mass, b3.mass, d23)
    f13 = Gravitational_Force(b1.mass, b3.mass, d13)

    f12x = f12*(b1.px - b2.px) / 2
    f12y = f12*(b1.py - b2.py) / 2
    f23x = f23*(b2.px - b3.px) / 2
    f23y = f23*(b2.py - b3.py) / 2
    f13x = f13*(b1.px - b3.px) / 2
    f13y = f13*(b1.py - b3.py) / 2

#Updating positions
    b1.px, b1.py, b1.vx, b1.vy = Motion(b1.px, b1.py, b1.vx, b1.vy, (-f12x-f13x)/b1.mass, (-f12y-f13y)/b1.mass)
    b2.px, b2.py, b2.vx, b2.vy = Motion(b2.px, b2.py, b2.vx, b2.vy, (f12x-f23x)/b2.mass, (f12y-f23y)/b2.mass)
    b3.px, b3.py, b3.vx, b3.vy = Motion(b3.px, b3.py, b3.vx, b3.vy, (f23x+f13x)/b3.mass, (f23y+f13y)/b3.mass)


#Drawing trajectory
    Trajectory(turtle1, b1.px, b1.py, 'blue', b1.mass / (max(b1.mass, b2.mass, b3.mass)))
    Trajectory(turtle2, b2.px, b2.py, 'red', b2.mass / (max(b1.mass, b2.mass, b3.mass)))
    Trajectory(turtle3, b3.px, b3.py, 'green', b3.mass / (max(b1.mass, b2.mass, b3.mass)))