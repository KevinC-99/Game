
import random
import turtle

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

def Order(players):
    
    tempNums = []

    for i in range(len(players)):
        roll = random.randint(0, 6)
        tempNums.append(roll)

    return(tempNums)
    
turns = []
turns = Order(players)

def drawDice():

    turtle.Screen().exitonclick()

def diceRollOne():
    turtle.hideturtle()
    turtle.speed(0)
    for i in range(4):
        turtle.pendown()
        turtle.forward(100)
        turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.right(90)
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    turtle.Screen().exitonclick()
    