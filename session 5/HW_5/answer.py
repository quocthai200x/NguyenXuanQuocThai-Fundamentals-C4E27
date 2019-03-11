1.why should we use functions at all ?
Bởi vì khi code ta có thể dùng lặp lại 1 khối lệnh ở các vị trí khác nhau ,
 việc dùng hàm sẽ tiết kiệm thời gian hơn vì chỉ cần thay tên hàm là đc thay vì gõ lại cả
 khối lệnh 

2.How to define/declare a function?
def tên hàm ( tham số(có thể có hoặc không) ):
#    Mô tả ngắn về hàm
   codes ...
   return (có thể có có hoặc không)

3.How to call/use a function? 
vd : def call(tham số nếu có):
    khối lệnh

call(tham số nếu có)

4.What is return, why and how do we use it?
Lệnh return dùng để trả về một giá trị (hoặc một biểu thức), hoặc đơn giản là trả về không gì cả 
Thế nên , nếu ta cần giá trị của 1 hàm sau khi thực hiện khối lệnh trong hàm thì ta phải có return

5.Do we have to use return in every function? 
Ta dùng return khi ta cần giá trị , thế nên đối vs hàm mà ta ko cần ra giá trị thì ta không cần dùng return
vd :
def no_return():
    print('abc')
no_return() 

6.What are function arguments/parameters, why and how we use it?
Tham số là các giá trị mà mình tùy ý nhập vô . Chúng ta dùng tham số để gắn các giá trị vào các lệnh trong
hàm 
vd :
def thamso(n):
    return n+1
n = int(input('nhập số'))
print(thamso(n))

7.How to use function from a different file other than our currently working file?
vd :
ta có 1 tập py tên python1.py và trong đó có hàm tên: function()
sang tập py tên python2.py
gõ : 
from python1 import function() 
function()

