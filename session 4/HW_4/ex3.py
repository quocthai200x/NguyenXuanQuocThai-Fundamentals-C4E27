
ans ={'1.': 35,'2.':36,'3.':40,'4.':44}
while True :
    print('If x = 8 , then what is the value of 4(x +3) ?')
    for k ,v in ans.items() :
        print(k,v)
    n = input('your answer ? Type exit or quit to get out :  ')
    if n == '4' :
        print('bingo')
        
        k = input('do u want to play again ?yes or no : ')
        while not k in ['yes','no'] :
            k = input('sai cú pháp , please type yes or no : ')
        if k == 'yes':
            print()
        elif k == 'no' :
            break 
        
    elif n in ['exit','quit']:
        break
    elif  n in ['2','3','1'] :
        print('sai r :(')
    else :
        print('cú pháp ko hợp lệ hoặc ngoài tầm đáp , mời nhập lại')
