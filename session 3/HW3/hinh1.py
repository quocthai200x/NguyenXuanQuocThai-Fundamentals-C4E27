from turtle import * 

mau = ['red','blue','brown','yellow','grey']
goc = [120,90,72,60,360/7]
for i in range (5):
        color(mau[i])
        for j in range (1,i+4):
                forward(100)
                left(goc[i])
mainloop()