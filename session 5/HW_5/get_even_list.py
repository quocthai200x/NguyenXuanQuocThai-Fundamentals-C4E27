def get_even_list(ls):
    for  i in list(ls) :
        if i%2 != 0  :
           ls.remove(i)
    return ls 
ls = [1, 4, 5, -1, 10]
print(ls)
print(get_even_list(ls))


even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

