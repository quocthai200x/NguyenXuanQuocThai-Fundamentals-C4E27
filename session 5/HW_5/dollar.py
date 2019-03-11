def dollar (s):
    newstr = s.replace('$','')
    return newstr
s = input('nhập tiền với $ : ')
print(dollar(s))
string_with_no_dollars = dollar("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
