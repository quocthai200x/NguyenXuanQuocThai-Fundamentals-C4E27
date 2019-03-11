from is_inside import is_inside
from is_inside import hinh
dem = 0
for x in range (-200,200):
    pos =[]
    pos.append(x)
    for y in range (-100,200):
        pos.append(y)
        if is_inside(pos,hinh) == False :
            dem += 1
if dem != 0 :
    print('chạy ngon r')
else : 
    print('chất điểm ngoài hình mà không ngoài hình')