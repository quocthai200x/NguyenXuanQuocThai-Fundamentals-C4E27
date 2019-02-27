n = int(input('mời nhập 1 số  : '))
y=1
for x in range (1,n+1) :
   y=y*x
if  n == 1 :
    print ('mời bạn lắp thêm não ạ , kết quả bằng 1 ') 
elif n==2 :
    print (' wow , bạn nhập số 2 thì giỏi vl , 2x1=2  thôi mà ??')
else:
    print ('giai thừa của ',n,'là :',y)