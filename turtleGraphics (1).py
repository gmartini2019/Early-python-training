import turtle
s = turtle.getscreen()
t = turtle.Turtle()
turtle.title("Giulio's turtle program")



#PROBLEM N.1

#t.goto(40,0)
#t.goto(0,80)
#t.goto(-40,0)
#t.goto(0,0)


#PROBLEM N.2


#t.color("blue")
#t.forward(100)
#t.left(120)
#for i in range(6):
  
 # t.forward(100)
  #t.left(60)
  
#t.color("white")
#t.home()
#t.color("black")


#PROBLEM N.3

#def drawRectangle(t, w, h):
   
   #t.color("red", "yellow")
   #t.pencolor("red")
   #t.fillcolor("yellow")
   #for i in range(2):
    #  t.forward(w)
    # t.left(90)
    #  t.forward(h)
    #  t.left(90)
   #t.left(90)
   #turtle.Screen().exitonclick()
   


#w = int(input("Enter width: "))
#h = int(input("Enter height: "))
#drawRectangle(t, w, h)

   

  



#PROBLEM N.4

#def drawRectangle2(t, w, h, j,i, colors):
   
#   t.color("red", "yellow")
#   t.pencolor("red")
#   color1 = colors[0]
#   color2 = colors[1]
#   if(i%2 == 0):
#      if(j%2 == 0):
#               
#               t.fillcolor(color1)
#               t.begin_fill()
#      else:
#               t.fillcolor(color2)
#               t.begin_fill()
#   else:
#      if(j%2 == 0):
#               t.fillcolor(color2)
#               t.begin_fill()
#      else:
#               t.fillcolor(color1)
#               t.begin_fill()
#   for i in range(2):
#      t.forward(w)
#      t.left(90)
#      t.forward(h)
#      t.left(90)



#def drawChessBoard(t, size, colors):
#   t.speed(100)
#   for i in range(8):
#      if(i != 0):
#         t.backward(160)
#         t.left(270)
#         t.forward(20)
#         t.left(90)
#
#      for j in range(8):
#        
#         drawRectangle2(t, 20, 20, j,i, colors)
#         t.end_fill()
#         t.forward(20)
#   turtle.Screen().exitonclick()


#size = int(input("Enter size of square: "))
#colors = ('yellow', 'blue')
#drawChessBoard(t,10, colors)



