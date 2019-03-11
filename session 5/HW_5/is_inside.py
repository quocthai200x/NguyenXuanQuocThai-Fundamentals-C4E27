def is_inside(pos,hinh):
    if hinh[0] <=pos[0]<= hinh [0]+ hinh[2]:
        if hinh[1] <= pos[1] <= hinh[1] + hinh[3] :
            return True
        return False
    else :
        return False
pos = [300,400]

hinh = [3,4,100,200]
is_inside(pos,hinh)
print(is_inside(pos,hinh))
