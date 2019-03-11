# # # # # # n = int(input('nhập tổng số'))
# # # # # # ls = []
# # # # # # for i in range (n):
# # # # # #     m = int(input('nhập số'))
# # # # # #     ls.append(m)
# # # # # # tong = 0
# # # # # # for k in ls :
# # # # # #     tong = tong + k
# # # # # # print('tổng dãy số vừa nhập là : ',tong)

# # # # # # a = int(input('nhập tổng số'))
# # # # # # ls1 = []
# # # # # # for j in range (a):
# # # # # #     o = int(input('nhập số'))
# # # # # #     ls1.append(o)
# # # # # # tong1 = 0
# # # # # # for b in ls1 :
# # # # # #     tong1 = tong1 + b

# # # # # # tbc = tong1/n
# # # # # # print('trung bình cộng là',tbc)


# # # # # # HÀM
# # # # # def say_hi():
# # # # #     print('hi')
# # # # #     print('bye')
# # # # # say_hi()
# # # # # say_hi()
# # # # # say_hi()
# # # # # say_hi()
# # # # # say_hi()
# # # # # say_hi()
# # # # # say_hi()



# # # # def add_two_numbers(a,b):
# # # #     return a +b
    
# # # # num1 = int(input('số 1 : '))
# # # # num2 = int(input('số 2 : '))
# # # # num3 = int(input('số 3 : '))
# # # # sum1_2 = add_two_numbers(num1,num2)
# # # # sum_3 = add_two_numbers(sum1_2,num3)
# # # # print('tổng 3 số : ', sum_3)

# # # def add_two_numbers(a,b):
# # #     print(a +b)
    
# # # print(add_two_numbers(3,4))

# # def abs_of_number(a):
# #     if a> 0 : 
# #         return a
# #         print('trị tuyệt đối là :',a)
# #     else : 
# #         return  -a
# #         print('trị tuyệt đối là :',-a)
# #     print('trị tuyệt đối  là : ',a)
# # x= abs_of_number(-12)
# # tong =12 +abs_of_number(-12)
# # print(x,tong)


# def evaluate(a,b,x) :
#     return eval(a+x+b)
# num1 = str(input('số thứ 1 : '))
# num2 = str(input('số thứ 2 : '))
# dau =  str(input())
# print(evaluate(num1,num2,dau))

# # còn có thể dùng if cho mỗi dấu (tự làm đi )


def songuyento(n):
    if n <2 :
        return False
 
    for v in range (2,n):
        if n%v ==  0  :
            return False 
        return True

# if songuyento(n):
#     print('ko la so nguyen to ')
# else :
#     print( 'là sô ngyên tố')
# print(ls)
so = int(input('nhập số cần kiểm tra'))
for v  in range (2,so +1):
    if songuyento(v) :
        print('số nguyên tố là : ',v,end='')

