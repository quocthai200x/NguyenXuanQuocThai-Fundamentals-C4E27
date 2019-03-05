from turtle import * 

mau = ['red','blue','brown','yellow','grey']

for hinh in range (5):
    color(mau[hinh])
    begin_fill()
    # vẽ hình chữ nhật
    for i in range (2):   
        for cn in range (1,3):          
            forward(50*cn)
            right(90)
    end_fill()
    forward(50)
mainloop()