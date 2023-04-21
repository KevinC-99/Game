import random
import turtle
import time

def rollDice():
    roll = random.randint(0, 6)
    return(roll)

def creatingPlayers():

    tempArray = []

    while True:
        try:
            numOfPlayers = int(input("How many people are playing?: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    for i in range(numOfPlayers):
        name = input("Enter the players name: ")
        tempArray.append(name)
    tempArray.sort()
    return(tempArray)

players = []
players = creatingPlayers()

def drawDiceBorder():
    turtle.tracer(0)
    turtle.hideturtle()
    turtle.speed(0)
    for i in range(4):
        turtle.pendown()
        turtle.forward(100)
        turtle.left(90)

def drawTwoDots():
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.pendown()
    turtle.right(90)
    drawCircle()
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    drawCircle()

def drawCircle():
    turtle.tracer(1)
    turtle.speed(0)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def diceRollOne():
    drawDiceBorder()
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.right(90)
    drawCircle()

def diceRollTwo():
    drawDiceBorder()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    drawTwoDots()

def diceRollThree():
    drawDiceBorder()
    drawTwoDots()
    turtle.penup()
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.pendown()
    drawCircle()

def diceRollFour():
    drawDiceBorder()
    drawTwoDots()
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(85)
    turtle.left(90)
    turtle.pendown()
    drawTwoDots()

def diceRollFive():
    drawDiceBorder()
    drawTwoDots()
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(85)
    turtle.left(90)
    turtle.pendown()
    drawTwoDots()
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(85)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    turtle.right(90)
    drawCircle()

def diceRollSix():
    drawDiceBorder()
    drawTwoDots()
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(85)
    turtle.left(90)
    turtle.pendown()
    drawTwoDots()
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    drawTwoDots()

def Order(players):
    
    movement = 0
    tempNums = []
    turtle.setup(width=1080, height=720)
    turtle.hideturtle()
    turtle.write("Rolls are done Alphabetically (Names)", align="center", font=("Ariel", 32, "normal"))
    time.sleep(3)
    turtle.undo()
    turtle.write("First Player!", align="center", font=("Ariel", 32, "normal"))
    time.sleep(3)
    turtle.undo()
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    for i in range(len(players)):
        roll = random.randint(1, 6)
        if roll == 1:
            tempNums.append(roll)
            diceRollOne()
        elif roll == 2:
            tempNums.append(roll)
            diceRollTwo()
        elif roll == 3:
            tempNums.append(roll)
            diceRollThree()
        elif roll == 4:
            tempNums.append(roll)
            diceRollFour()
        elif roll == 5:
            tempNums.append(roll)
            diceRollFive()
        elif roll == 6:
            tempNums.append(roll)
            diceRollSix()
        turtle.penup()
        turtle.goto(0, 200)
        turtle.hideturtle()
        turtle.write("Next Player!", align="center", font=("Ariel", 32, "normal"))
        time.sleep(3)
        turtle.undo()
        turtle.goto(-200, 0)
        for j in range(1):
            movement += 120
        turtle.forward(movement)
        turtle.pendown()
        turtle.update()
    turtle.done()

    return(tempNums)
    
turns = []
turns = Order(players)

print(players)
print(turns)