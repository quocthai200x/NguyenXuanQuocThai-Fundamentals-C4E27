# game = [' b k o o','u e l i m t a t','t e k d s c h i']
# i = str(input('Hãy chọn 1 con số từ 1 đến 3 :  '))
# num = ['1','2','3']
# while not i in num :
#     print('try')
#     i =str(input())
# while  i == '1':
#     print('k o b o')
#     ans = input('câu trả lời của bạn : ')
#     if ans == 'book':
#         print('mới bắt đầu thôi thử số 3 đi')
#         break
#     else :
#         print('thử lại đi , gợi ý là giấy và học')
#         break
# while  i == '2':
#     print('u e l i m t a t')
#     ans = input('câu trả lời của bạn : ')
#     if ans == 'ultimate':
#         print('có vẻ chơi liên minh nhiều ')
#         break
#     else :
#         print('Sai òi bạn ơi , một từ ko thể lạ vs game moba')
#         break
# while  i == '3':
#     print('t e k d s c h i')
#     ans = input('câu trả lời của bạn : ')
#     if ans == 'techkids':
#         print('yeah :)))))))))))))))))))')
#         break
#     else :
#         print('tip : học ở đâu đấy')
#         break





import random

print("WORD GAME")
print()
print("Rules: you have to correct words by arranging letters given below")
# print("there are 2 level")

# lv=int(input("choose your level: "))


lv1=['apple','orange','grape']
lv2=['crab','fish','lobster']
# lv3=['football','volleyball','parachuting']
# lv4=['policeman','carpenter','firefighter']
# lv5=['psychology','diversity']
# lv6=['rhinoceros','elephant','megalodon']
# for i in range(len(lv2)):
#         q=list(lv2[i])

#         random.shuffle(q)
#         print(q)
#         ans = str(input("answer: "))

for i in range(len(lv1)):
    
        q=list(lv1[i])

        random.shuffle(q)
        print(*q)
        ans = str(input("answer: "))
        if ans == (lv1[i]):
            print("right, but just very simple")
        else:
            break
        
    


