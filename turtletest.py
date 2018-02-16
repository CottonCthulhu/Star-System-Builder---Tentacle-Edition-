import turtle
from random import randint
import math

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def getNewTurtle():
    localTurtle = turtle.Turtle()
    localTurtle.hideturtle()
    localTurtle.speed(6)
    return localTurtle

def moveTurtleToPosition(turtle, x, y):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()

def getRandomColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return Color(r, g, b)

def setTurtleToColor(turtle, color):
    turtle.screen.colormode(255)
    turtle.color(color.r, color.g, color.b)

def getPointOnCircle(radius, steps, n = 360):
    x = math.cos(2 * math.pi / n * steps) * radius
    y = math.sin(2 * math.pi / n * steps) * radius
    return Point2D(x,y)

def drawFilledCircle(turtle, x, y, radius):
    moveTurtleToPosition(turtle, x, y)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def getBottomYOfScreenPositionForTurtle(turtle):
    return -turtle.screen.window_height() / 2

def drawPlanetaryOrbit(orbitRadius):
    localTurtle = getNewTurtle()
    moveTurtleToPosition(localTurtle,
                         0,
                         getBottomYOfScreenPositionForTurtle(localTurtle) - orbitRadius)
    localTurtle.circle(orbitRadius)

def getPositionForPlanet(orbitRadius, orbitAngle):
    planetTurtle = getNewTurtle()
    planetPos = getPointOnCircle(orbitRadius, orbitAngle)
    planetPos.y += getBottomYOfScreenPositionForTurtle(planetTurtle)
    return planetPos

def drawPlanet(planetPosition, orbitRadius, planetRadius, planetDescription, color = Color(0,0,0)):
    drawPlanetaryOrbit(orbitRadius)
    planetTurtle = getNewTurtle()

    moveTurtleToPosition(planetTurtle,
                         planetPosition.x + planetRadius + 5,
                         planetPosition.y + planetRadius)
    planetTurtle.write(planetDescription)

    setTurtleToColor(planetTurtle, color)
    drawFilledCircle(planetTurtle,
                     planetPosition.x,
                     planetPosition.y - planetRadius,
                     planetRadius)

def drawMoon(planetPosition, orbitRadius, moonRadius, color = Color(0,0,0)):
    moonTurtle = getNewTurtle()
    moveTurtleToPosition(moonTurtle,
                         planetPosition.x,
                         planetPosition.y - orbitRadius)
    moonTurtle.pensize(0.01)
    moonTurtle.circle(orbitRadius)

    moonPos = getPointOnCircle(orbitRadius, randint(0, 360))
    moonPos.x += planetPosition.x
    moonPos.y += planetPosition.y

    setTurtleToColor(moonTurtle, color)
    drawFilledCircle(moonTurtle,
                     moonPos.x,
                     moonPos.y - moonRadius,
                     moonRadius)

def drawStellarBody(stellarBodyRadius):
    stellarTurtle = getNewTurtle()
    drawFilledCircle(stellarTurtle,
                     0,
                     getBottomYOfScreenPositionForTurtle(stellarTurtle) - stellarBodyRadius,
                     stellarBodyRadius)

stellarBodyRadius = randint(40,50)

drawStellarBody(stellarBodyRadius)

for i in [2,4,6]:
    orbitRadius = 100 + int(math.pow(i, 2) * 10)
    planetPos = getPositionForPlanet(orbitRadius, randint(60,120))
    planetRadius = randint(5,30)
    drawPlanet(planetPos, orbitRadius, planetRadius, "HANS " + str(i))
    for i1 in range(4,randint(4,12), 3):
        orbitRadius = planetRadius + int(i1 * 2)
        moonRadius = randint(2, 3)
        drawMoon(planetPos, orbitRadius, moonRadius)


saveTurtle = turtle.Turtle()
saveTurtle.hideturtle()
ps = saveTurtle.screen.getcanvas().postscript(file = 'test.eps', colormode = 'color')

turtle.mainloop()