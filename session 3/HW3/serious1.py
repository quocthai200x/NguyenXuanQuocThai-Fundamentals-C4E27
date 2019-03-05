print('Chào mừng đến vs cửa hàng , bạn muốn gì ạ ? ')
print('Ấn r để xem sản phẩm')
print('Ấn c để thêm sản phẩm ')
print('Ấn u để thay thế sản phẩm ')
print('Ấn d để xóa sản phẩm')
quanao = ['T-shirt','Sweater']
print('Các sản phẩm đang có là : ')
print(quanao)
n = str(input())

options =['r','c','u','d']
while n not in options : 
    print('hãy ấn lại hoặc r,c,u,d để tiếp tục')
    n = str(input())

if n == 'r' :
    print('Danh sách sản phẩm là : ')
    print(quanao)
elif n =='c' :
    print('Enter new item')
    new = str(input())
    quanao.append(new)
    print ('Danh sách sản phẩm là : ')
    print (quanao)
elif n == 'u':
    upd= int(input('Update position ? : '))
    ps = upd -1
    quanao.pop(ps)
    item = str(input('New item ? : '))
    quanao.insert(ps,item)
    print('Danh sách sản phẩm là : ')
    print(quanao)
else :
    delete = int(input('Delete position ? : '))
    quanao.pop(delete-1)
    print('Danh sách sản phẩm là : ')
    print(quanao)
    