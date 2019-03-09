ans1 ={'1.': 35,'2.':36,'3.':40,'4.':44}
ans2 = {'1.':'About 55','2.':'About 65','3.':'About 75','4.':'About 85'}
while True :
    print('If x = 8 , then what is the value of 4(x +3) ?')
    i = 0
    while True :
        for k ,v in ans1.items() :
            print(k,v)
        n = input('your answer ? 1,2,3 or 4 :  ')
        if n == '4' :
            print('bingo')
            i = i + 1
            break
        elif  n in ['2','3','1'] :
            print('sai r :(')
            break
        else :
            print('cú pháp ko hợp lệ hoặc ngoài tầm đáp , mời nhập lại')
    while True :
        print('Jack scored these marks in 5 math tests :39,81,72,66 and 55 . What is the mean ?')
        for k1,v1 in ans2.items() :
            print(k1,v1)
        m = input('your answer ? 1,2,3 or 4 :  ')
        if m == '2' :
            print('bingo')
            i = i + 1
            break
        elif  m in ['4','3','1'] :
            print('sai r :(')
            break
        else :
            print('cú pháp ko hợp lệ hoặc ngoài tầm đáp , mời nhập lại')
    print('Your correctly answer',i,'out of 2 questions')

    k = input('do u want to play again ?yes or no : ')
    while not k in ['yes','no'] :
        k = input('sai cú pháp , please type yes or no : ')
    if k == 'yes':
            print()
    elif k == 'no' :
        break 
