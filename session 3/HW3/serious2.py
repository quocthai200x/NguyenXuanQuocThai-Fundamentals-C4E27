sizes = [5,7,300,90,24,50,75]
print('The sizes of the sheep : ')
print (sizes)
print()





print() 
# lấy con lớn nhất 

print('Now my biggest sheep has ',max(sizes),'.Let us shear it ')






# lấy con lớn nhất rồi thêm con mới kích cỡ 8 
p = sizes.index(max(sizes))
sizes.remove(max(sizes))
sizes.insert(p,8)
print('After shearing, here is my flock')
print(sizes)
print()
print()




# 1 tháng
print('Month 1 :')
onemonth = [x+50 for x in sizes] 
print ('One month has passed, now here is my flock')
print (onemonth)











# n tháng 
print()
print()
# bài 2.5 khác vì ko lấy max ngay mà sau 1 tháng mới lấy nên đặt list mới
print('Hello , my name is Hiep and here is my flock')
size = [5,7,300,90,24,50,75]
print(size)
n = input('nhập số tháng : ')
while not n.isdigit():
    print('Hãy nhập lại số tháng : ')
    n = input()
n= int(n)
for i in range (1,n+1):
    print('Month',i,':')
    size = [y+50 for y in size ]
    print ('One month has passed, now here is my flock')
    print(size)
    print ('Now my biggest sheep has size',max(size),' let us shear it')
    q = size.index(max(size))
    size.remove(max(size))
    size.insert(q,8)
    print('After shearing, here is my flock')   
    print(size)
    print()






# tính tiền theo nếu nuôi n tháng 
print('Hello , my name is Hiep and here is my flock')
size =[5,7,300,90,24,50,75]
print(size)
print()
print ('Now my biggest sheep has size',max(size),' let us shear it')
k = size.index(max(size))
size.remove(max(size))
size.insert(k,8)

n = input('nhập số tháng : ')
while not n.isdigit():
    print('Hãy nhập lại số tháng : ')
    n = input()
n= int(n)
for i in range (1,n):
    print('Month',i,':')
    size = [y+50 for y in size ]
    print ('One month has passed, now here is my flock')
    print(size)
    print ('Now my biggest sheep has size',max(size),' let us shear it')
    q = size.index(max(size))
    size.remove(max(size))
    size.insert(q,8)
    print('After shearing, here is my flock')   
    print(size)
    print()
size = [p+50 for p in size ]

print('Month',n,':')

print('My flock has size in total : ',sum(size))
print('I would get',sum(size),'*2$ = ',sum(size)*2)






