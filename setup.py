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
    turtle.Screen().exitonclick()

def diceRollTwo():
    drawDiceBorder()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    drawTwoDots()
    turtle.Screen().exitonclick()

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
    turtle.Screen().exitonclick()

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
    turtle.Screen().exitonclick()

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
    turtle.Screen().exitonclick()

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
    turtle.Screen().exitonclick()

def Order(players):
    
    tempNums = []

    for i in range(len(players)):
        roll = random.randint(0, 6)
        if roll == 1:
            diceRollOne()
            tempNums.append(roll)
        elif roll == 2:
            diceRollTwo()
            tempNums.append(roll)
        elif roll == 3:
            diceRollThree()
            tempNums.append(roll)
        elif roll == 4:
            diceRollFour()
            tempNums.append(roll)
        elif roll == 5:
            diceRollFive()
            tempNums.append(roll)
        elif roll == 6:
            diceRollSix()
            tempNums.append(roll)

    return(tempNums)
    
turns = []
turns = Order(players)