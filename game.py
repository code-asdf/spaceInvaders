import turtle
import os

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.lt(90)

playerspeed = 15  # changeable

#Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 2

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(-5,.5)
bullet.hideturtle()

bulletspeed = 20

#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")


#Main game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x+=enemyspeed
    if x > 280 or x < -280:
        enemyspeed *= -1
        enemy.sety(enemy.ycor()-40)
    enemy.setx(x)

turtle.exitonclick()

# delay = input("Enter to continue")