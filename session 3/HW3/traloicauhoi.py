# 1.What is nested list?
# A nested list is a list that appears as an element in another list. In this list, the element with index 3 is a nested list:
# >>> nested = ["hello", 2.0, 5, [10, 20]]
# If we output the element at index 3, we get:
# >>> print(nested[3])
# [10, 20]
# To extract an element from the nested list, we can proceed in two steps:
# >>> elem = nested[3]
# >>> elem[0]
# Or we can combine them:
# >>> nested[3][1]
# 20
# Bracket operators evaluate from left to right, so this expression gets the 3’th element of nested and extracts the 1’th
# element from it.

# 2.Can a list store both integers and strings in it?
# Yes ,it can .
# For ex: 
#     ls =[1,'a',32434,'12345']
#     print(ls)