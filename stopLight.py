import turtle
turtle.setup(400, 600)
window = turtle.Screen()
window.title("STOP LIGHT EXERCISE")
window.bgcolor("pink")
green = turtle.Turtle()
yellow = turtle.Turtle()
red = turtle.Turtle()
def drawLightFrame ():
    green.pensize(3) 
    green.color('black', 'white')  
    green.begin_fill()  
    green.forward(80)  
    green.left(90)  
    green.forward(200)
    green.circle(40, 180)  
    green.forward(200)
    green.left(90)
    green.fillcolor('black')
    green.end_fill()  

drawLightFrame()

def circle(t, ht, colr):
    t.penup()  
    t.forward(40)
    t.left(90)
    t.forward(ht)
    t.shape('circle')  
    t.shapesize(3)  
    t.fillcolor(colr)  

circle(red,50, 'green')
circle(yellow, 120, 'yellow')
circle(green, 190, 'red')
state = 0

def stateMachineStopLight():
   global state 

   if state == 0:  
        green.color('darkgrey')
        yellow.color('darkgrey')
        red.color('green')
        window.ontimer(stateMachineStopLight, 3000)  
        state = 1
   elif state == 1: 
        green.color('darkgrey')
        yellow.color('orange')
        window.ontimer(stateMachineStopLight, 1000)
        state = 2
   elif state == 2: 
        red.color('darkgrey')
        window.ontimer(stateMachineStopLight, 1000)
        state = 3
   else:                 
        green.color('red')
        yellow.color('darkgrey')
        window.ontimer(stateMachineStopLight, 2000)
        state = 0


stateMachineStopLight()

window.listen()  

window.mainloop()  