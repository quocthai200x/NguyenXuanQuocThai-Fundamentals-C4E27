
prices = {}
prices['banana']= 4
prices["apple"]= 2
prices["orange"]= 1.5
prices["pear"]= 3
print(prices)

stock = {}
stock['banana']=6
stock["apple"]= 0
stock["orange"]= 32
stock["pear"]=15
print(stock)
y=0
for k,v in prices.items():
    for k1,v1 in stock.items() :
        if k == k1 :
            print(k1,':')
            print(prices[k])
            print(stock[k1])
            total = prices[k]*stock[k1]
            y=y+total 
print(y)        
