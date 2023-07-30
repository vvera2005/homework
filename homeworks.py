#!/usr/bin/python3

# Dictionary 19

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = {}
# for k,v in d1.items():
#     if k in d2.keys():
#        d3[k] = d1[k] + d2[k]
#     else :
#         d3[k] = d1[k]
# for k,v in d2.items():
#     if d2[k] not in d1.keys():
#         d3[k] = d2[k]
# print(d3)

# Dictionary 23 Write a Python program to combine values in a list of dictionaries.

# ml = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# res = {}

# for dict in ml:
#     item = dict["item"]
#     amount = dict["amount"]

#     if item in res:
#         res[item] = res[item] + amount
#     else:
#         res[item]= amount

# print(res)

# Dictionary 30. Write a Python program to get the top three items in a shop.

# md = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

# top_3 = {}

# values = sorted(md.values())[::-1]

# while values:
#     for k,v in md.items():
#         if v == values[0]:
#             top_3[k] = v  
#             values  = values[1:]

# for i, (k, v) in zip(range(3), top_3.items()):
#     print(k,v)


#List15. Write a Python program to shuffle and print a specified list.

# ml = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# temp = set(ml)
# ml = list(temp)
# print(ml)

# List 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

# ml = []
# for i in range(1,31):
#     ml.append(i**2)

# print(ml[:5], ml[-5:])

#List 19. Write a Python program to calculate the difference between the two lists.

# ml1 = [1,5,6,9,58,4,6,7]
# sum = 0
# ml2 = [6,5,4,8,6,1,5,151,51]
# ml3 = []
# for el in ml1:
#     if not el in ml2:
#         ml3.append(el)
# for el in ml3:
#     sum += el
# print(sum)

# import signal
# import time
# import random

# countries = {
#         "Armenia" : "Yerevan",
#         "France" : "Paris",
#         "China" : "Pekin",
#         "USA" : "Washington",
#         "Brazil" : "Brazil"
# }

# ml = list(countries.items())

# random.shuffle(ml)
# count = 3

# for el in ml:
#     print('What is the capital of %s' % el[0])
#     if (count == 0):
#         print('Game over')
#         break
#     answer = input('Enter your answer: ')
#     if answer.lower() == el[1].lower():
#         print('Correct!'); 
#     else:
#         count -= 1
#         print('Incorrect.You have %d attend' %count)


# funktions

# 1. replace

# def my_replace(mstr, what, with_what):
#     res = ""
#     if type(mstr) != str:
#         print("Only string conteiner")
#         return None
#     else:
#         for el in mstr:
#             if el == what:
#                 res += with_what
#             else:
#                 res += el
#         return res

# print(my_replace("Hello world","e","k"))

# 2. find

# def my_find(mstr, symb):
#     if type(mstr) != str:
#         print("Only string conteiner")
#         return None
#     else:
#         for i in range(len(mstr)):
#             if mstr[i] == symb:
#                 return i

# print(my_find("hello world", 5))

# 3. upper

# def my_upper(mstr):
#     uppercase = ""
#     if type(mstr) != str:
#         print("Only string conteiner")
#         return None
#     else:
#         for el in mstr:
#             if el.isalpha():
#                 uppercase += chr(ord(el) - 32)
#             else:
#                 uppercase += el
#     return uppercase

# print(my_upper("hello world"))

# 4. strip

# def my_strip(string):
#     start = 0
#     end = len(string) - 1
#     while start <= end and string[start].isspace():
#         start += 1
#     while start <= end and string[end].isspace():
#         end -= 1
#     return string[start:end + 1]

# print(my_strip("   Hello world     "))

# 5. capitalize

# def my_cap(string):
#     for i in range(len(string)):
#         if string[i].isalpha():
#             return string[:i] + chr(ord(string[i]) - 32) + string[i+1:]

# print(my_cap("   hello world"))

# 6. isalpha

# def my_isapha(string):
#     if type(string) != str:
#         print("Only string conteiner")
#         return None   
#     else: 
#         for el in string:
#             if not ("a" <= el <= "z" or "A" <= el <= "Z"):
#                 return False
#         return True

# print(my_isapha(53))

# 7. count()

# def my_count(mstr, letter):
#     cnt = 0
#     if type(mstr) != str:
#         print("Only string conteiner")
#         return None
#     else:
#         for i in range(len(mstr)):
#             if mstr[i] == letter:
#                 cnt += 1
#     return cnt

# print(my_count("hello world" , "o"))

# or when more than one item can be

# def my_count(mstr, word):
#     cnt = 0
#     if type(mstr) != str or type(word) != str:
#         print("Only string conteiner")
#         return None
#     else:
#         for i in range(len(mstr)- len(word) + 1):
#             if mstr[i:i + len(word)] == word:
#                 cnt += 1
#     return cnt

# print(my_count("hello world" , "or"))

# 8. startwith()

# def my_start_with(string, el):
#     if type(string) != str or type(el) != str:
#         print("Only string conteiner")
#         return None
#     else:
#         if string[ : len(el)] == el:
#             return True
#         return False
    
# print(my_start_with(" Hello world", "Hel"))
# print(my_start_with("Hello world", "hel"))

# 9. islower()
# def my_islower(string):
#     if type(string) != str:
#         print("Only string conteiner")
#         return None  
#     else:
#         for el in string:
#             if not ("a" < el < "z" or el.isspace()):
#                 return False
#         return True
    
# print(my_islower("hello world"))
# print(my_islower("hello worlD"))

# 10. join

# def my_join(ml, jpart):
#     tmp = ""
#     if type(ml) != list:
#         print("Only list conteiner")
#         return None
#     else:
#         for el in ml:
#             tmp += el
#             tmp += jpart
#     return tmp

# print(my_join(["Hello",'World', 'Vera'], ","))

    
# Amenapoqr yndhanur bazmapatik, amenamec bajanarar


def baj(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

print(baj(18,30))

def bazm(a,b):
    tmp = baj(a,b)
    return a * b / tmp

print(bazm(18,30))