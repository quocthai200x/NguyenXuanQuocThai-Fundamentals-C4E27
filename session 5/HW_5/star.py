from turtle import *
speed(0)
bgcolor('black')
def star(x,y,lenght):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range (5):
        forward(lenght)
        right(144)
# x = int(input('tọa độ x : '))
# y = int(input('tọa độ y : '))
# lenght= int(input('nhập chiều dài : '))
# star(-50,50,100)
color('yellow')
for i in range(100):
    import random
    x = random.randint(-500,500)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    star(x, y, length)

mainloop()