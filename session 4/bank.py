money = int(input('tiền đang có : '))
year = int(input('năm nuôi tiền @@ : '))

for i in range (1,year+1):
    money = money + (6.5/100)*money
    print('số tiền qua',i,'năm : ',money) 

n = 0 
savemoney = int(input('tiền đang có : ' ))
while not savemoney > 1200000000 :
    savemoney =savemoney + (6.5/100)*savemoney
    n = n +1
print('số năm để tiết kiệm được 1,2 tỉ là ',n)

