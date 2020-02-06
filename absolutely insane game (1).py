import turtle
import random
import math
import time
sc = turtle.Screen()
sc.bgcolor("lightblue") #sets up bg
sc.tracer(3)

#sets up border
mypen = turtle.Turtle()
mypen.penup()
mypen.speed(0)
mypen.setposition(-875, -450)                                                    #have random or colour specific value of speed same as energyuse and food   #use alg.clear to remove from screen then oeform function of generating new after certain amount of time
mypen.pendown()
mypen.pensize(3)
for side in range (2):
    mypen.forward(1750)
    mypen.left(90)
    mypen.forward(900)
    mypen.left(90)
mypen.hideturtle()


player = turtle.Turtle() #sets up player
player.color("purple")
player.shape("triangle")
player.penup()
player.speed(0)

#setting up yel
yel = turtle.Turtle()
yel.color("yellow")
yel.shape("circle")
yel.penup()
yel.speed(0)
yelxpos = random.randint(-825, 825)
yelypos = random.randint(-400, 400)
yel.setposition(yelxpos, yelypos)


    
    
#defines some variable
speed = 0.75
hunger1 = 5








#sets up keyboard controls for player
def turnleft():      
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 0.75

def decreasespeed():
    global speed
    speed -= 0.75



#checks collision
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
     return  True
    else:
        return  False

#listens for controls
turtle.listen()
turtle.onkey(turnleft, "a")
turtle.onkey(turnright, "d")
turtle.onkey(increasespeed, "w")
turtle.onkey(decreasespeed, "s")






#grows algae
alg = []
for count in range(50):
    alg.append(turtle.Turtle())
    alg[count].penup()
    alg[count].color("green")
    alg[count].shape("circle")
    alg[count].speed(0)
    alg[count].shapesize(0.5)
    algxpos = random.randint(-825, 825)
    algypos = random.randint(-400, 400)
    alg[count].setposition(algxpos, algypos)
    

#defines coordinates of yel and alg
yelx = int(yel.xcor())
yely = int(yel.ycor())
algx = int(alg[count].xcor())
algy = int(alg[count].ycor())

    



    #BOUNDARY CHECKING
    #for player
while True:
    player.forward(speed)
    if player.xcor() > 875 or player.xcor() < -875:
         player.right(180)
        

    if player.ycor() > 450 or player.ycor() < -450:
        player.right(180)
        
        
    #for yel
    if yel.xcor() > 875 or yel.xcor() < -875:
        yel.right(180)

    if yel.ycor() > 450 or yel.ycor() < -450:
        yel.right(180)

    #COLLISION CHECKING
    #player and yel
    if isCollision(player, yel):
         yel.setposition(random.randint(-825, 825), random.randint(-400, 400))


    #unique yel + alg collisionn checking
    if yelx - algx <= 1 or yely - algy <= 1 or algx - yelx <= 1 or algy - yely <= 1:  #maxdistance may need changing. Could later be  mutated 
        hunger1 += 1
        alg[count].clear()
        time.sleep(5)                    #need to figure how to make algae respawn wait but not hunger change
        algxpos = random.randint(-825, 825)
        algypos = random.randint(-400, 400)
        alg[count].setposition(algxpos, algypos)
    
    
         
         
    



         
         


    #move cells
while True:
    yel.forward(2) #change to indiv + mutating factor later
    dturn1 = random.randrange(0, 101)
    if dturn1 == 1:
        yel.right(random.randrange(0, 181))
    elif dturn1 == 10:
        yel.left(random.randrange(0, 181))


   

          
   
        



    






    
          
            

























delay = input("Press enter to exit game")
