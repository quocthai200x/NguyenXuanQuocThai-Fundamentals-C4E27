from turtle import * 

# rua_chay_linh_tinh

shape("turtle")

speed (0)

for n in range (24):
    for i in range (4):
        forward(50)
        penup()
        forward(50)
        pendown()
        left(90)
    left(15)

for o in range (18):
    for u in range (2):
            penup()
            for p in range (90):
                forward(2)
                left(1)
            pendown()
            for y in range (90):
                forward(2)
                left(1)  
    left(20)              

mainloop()