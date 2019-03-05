# # # n = int (input("tổng chữ số cần tính  :  "))
# # # tong = 0
# # # for i in range (n) :
# # #     x = int(input('mời nhập các số : '))
# # #     tong = tong + x
# # # print ('tổng các chữ số đó là : ', tong)





# # # n = int(input('mời nhập số  : '))
# # # if n%2 == 1 :
# # #     print ('abc')
# # # else  : 
# # #     print ('ưhdiuashud')







# # # namsinh = int(input("mời nhập năm sinh của bạn  : "))
# # # age = 2019 - namsinh
# # # if  0 < age <10 : 
# # #     print ('you are baby')
# # #     print (age)
# # # elif age < 16 :
# # #     print ('you are teen')
# # #     print (age)
# # # else : 
# # #     print ('you are adult')
# # #     print (age)







# # yob = input('nhập năm sinh : ')

# # while  not yob.isdigit() : 
# #     print ('mày sai rồi ')
# #     yob = input('nhập lại năm sinh : ')

# # age =2019 - int(yob) 
# # print ( 'tuổi của bạn là : ',age)








# password = input('nhập pass : ')

# while True :
#     if len(password)>8 :
#         break
#     print('mật khẩu ko đc nhỏ hơn 8 kí tự ')
#     password = input('nhập lại pass : ')
# print('welcome to your home ')







# loopcount = 0 
# while True :
#     print ('loopcount : ', loopcount)
#     loopcount +=  1
#     if loopcount >= 3 : 
#         break
# print('abc')







# a = input('nhập số a : ')
# while  not a.isdigit () :
#     a = (input ("nhập lại số a"))

# b = input ('nhập số b : ')
# while  not b.isdigit () :
#     b = (input ("nhập lại số b "))

# c = input ('nhập số c : ')    
# while  not c.isdigit () :
#     c = (input ("nhập lại số c "))
# print (a,b,c)

# a= int(a)
# b= int(b)
# c= int(c)
# print (a+b+c)
# delta = (b*b) - (4*a*c)

# if delta > 0 :
#     x1 = (-b +delta**0.5)/(2*a)
#     x2 = (-b -delta**0.5)/(2*a)
#     print ('phương trình có 2 nghiệm riêng biệt là : ',x1 , x2)
        
# elif delta == 0 : 
#     print ('phương trình có 1 nghiệm duy nhát là : ',x)
# else : 
#     print ('phương trình vô nghiệm ')







ls=[]
n=int(input('nhập sô phần tử trong danh sách : '))
for i in range (n):
    print('nhập số phần tử thứ ',i+1) 
    so = int(input(''))
    ls.append(so)
print('dãy bạn vừa nhập là : ')
print (ls)
print()
print('tổng dãy số bạn vừa nhập là : ')
print(sum(ls))
print()
print('phần tử thứ 2 trong dãy là : ')
print (ls[1])


