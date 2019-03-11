from turtle import * 
speed(0)
def draw_square(lenght,a):
    color(a)
    for i in range(4):
        forward(lenght)
        left(90)
for  k in range (30) :
    draw_square(k*5,'red')
    left(17)
    penup()
    forward(k*2)
    pendown()
mainloop()        
