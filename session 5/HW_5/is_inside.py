def is_inside(pos,hinh):
    if hinh[0] <=pos[0]<= hinh [0]+ hinh[2]:
        if hinh[1] <= pos[1] <= hinh[1] + hinh[3] :
            print('the point is inside')
        else :
            print('the point is not inside')
    else :
        print('the point is not inside')
pos = [300,400]

hinh = [3,4,100,200]
is_inside(pos,hinh)

