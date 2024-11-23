import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0


#setting up the screen

window = turtle.Screen()
window.title("Snake game by Rv. ")
window.bgcolor("Black")
window.setup(width=1400 , height=1000)
window.tracer(0) #turns off the screen updates

#snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#00FFFF")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#FF69B4")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 460)
pen.write("Score: 0  High Score: 0", align = "center", font=("courier", 24, "normal"))

#functions

def go_up():
    if head.direction !="down":
        head.direction = "up"
    

def go_down():
    if head.direction !="up":
        head.direction = "down"
    

def go_left():
    if head.direction !="right":
        head.direction = "left"
    

def go_right():
    if head.direction !="left":
        head.direction = "right"
    


def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y= head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x= head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x= head.xcor()
        head.setx(x + 20)

#Keyboard Bindings

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

#main game loop

while True:
    window.update()

    #Check for collision with the border
    if head.xcor()>690 or head.xcor()<-690 or head.ycor()>490 or head.ycor()<-490:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000 , 1000)

        #Clear the segments
        segments.clear()

        #Reset the score
        score = 0

        #reset the delay
        delay = 0.1

        #Update the Score display       
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))


    #Check for the collision with the food
    if head.distance(food) < 20:

        #Move the food to the random spot.
        x = random.randint(-690, 690)
        y = random.randint(-490, 490)
        food.goto(x, y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#39FF14")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -= 0.001

        #Increase the Score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))

    #Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
    #Move segment 0 to where the head is.
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()

    #Check for the head collisions with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"


            #Hide the segments
            for segment in segments:
                segment.goto(1000 , 1000)

            #Clear the segments
            segments.clear()

            # Reset the score and delay
            score = 0
            delay = 0.1


            # Update the Score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))


    time.sleep(delay)

window.mainloop()
