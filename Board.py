## Start of the game
import turtle as t
import random


def square(i,j):
    colour = 'purple'

    random_int = random.randint(0,5)

    if random_int == 0:
        colour = 'blue'
    if random_int == 1:
        colour = 'magenta'
    if random_int == 2:
        colour = 'green'
    if random_int == 3:
        colour = 'yellow'
    if random_int == 4:
        colour = 'orange'
    if random_int == 5:
        colour = 'medium spring green'

    if i ==9 and j == 7:
        colour = 'red'
    if i == 6 and j == 3:
        colour = 'red'

    if i == 2 and j == 7:
        colour = 'white'

    if i == 3 and j == 2:
        colour = 'white'

    t.fillcolor(colour)
    t.begin_fill()

    for i in range(4):
        t.forward(20)
        t.left(90)

    t.end_fill()



def makeboard():
    t.hideturtle()
    t.speed(0)
    count = 0

    snakehead = []



    for i in range(10):
        t.penup()
        t.goto(0,count)
        t.pendown()
        count = count + 20
        for j in range(10):
            if i == 9 and j == 7:
                list = [t.xcor(), t.ycor()]
                snakehead.append(list)
            if i == 6 and j == 3:
                list2 = [t.xcor(), t.ycor()]
                snakehead.append(list2)
            square(i, j)
            t.forward(20)
    ladder1(snakehead)
    ladder2(snakehead)


def ladder1(head):

    t.penup()
    top1 = head[0]
    t.goto(top1[0]+5, top1[1]+5)
    t.pendown()
    t.right(110)
    t.forward(62)

    t.setheading(0)
    t.penup()
    t.goto(top1[0] + 15, top1[1] + 5)
    t.pendown()
    t.right(110)
    t.forward(62)

    for i in range(15):
        t.setheading(0)
        t.penup()
        t.goto(top1[0] + 15, top1[1] + 5)
        t.pendown()
        t.right(110)
        t.forward(4 * i + 1 )
        t.setheading(190)
        t.forward(10)



def ladder2(head):

    t.penup()
    top2 = head[1]
    t.goto(top2[0] + 5, top2[1] + 5)
    t.setheading(0)
    t.pendown()
    t.right(90)
    t.forward(140)


    t.penup()
    top2 = head[1]
    t.goto(top2[0] + 15, top2[1] + 5)
    t.setheading(0)
    t.pendown()
    t.right(90)
    t.forward(140)

    for i in range(35):
        t.setheading(0)
        t.penup()
        t.goto(top2[0] + 15, top2[1] + 5)
        t.pendown()
        t.right(90)
        t.forward(4 * i + 1 )
        t.setheading(190)
        t.forward(10)

makeboard()
t.Screen().exitonclick()


