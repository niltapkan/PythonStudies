# # Exercise
# # 0:
# #  - Write a program that consists of at least ten lines, 
# #  each of which has a logical statement on it. 
# #  The output of your program should be 5 Trues and 5 Falses.

# ls = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
# print('a' in ls)
# print('a' in 'ls')
# print('b' == 'c')
# print('k' < 'v')
# print('l' != 'b')
# print('b' + 'c' in ls)
# print('d' and 'f' in ls)
# print('d'.title() == ls)
# print(' ' in ls)
# print('a' and 'b' in ls)

# # 1 

# students = ['bedir', 'tarik', 'nilgun', 'huzeyfe', 'yusuf', 'jonas', 'diana', 'nilgun']
# if len(students) > 4:
#     print('The class is big enough')

# for student in students:
#     if len(student) > 5:
#         print(f'The letters here are to crowded: {student}')
#     elif student[0] == 'j':
#         print(f'Well who do we have here! Such a honor: {student}')
#     elif student[0] == 't':
#         print(f'..Why are you eben here... {student}')
#     else:
#         print(f'Well this one is just perfect: {student}')
# # 2

# manav = ['armut', 'elma', 'karpuz', 'muz', 'cilek']
# if len(manav) < 2:
#     print('Hadi ama yok mu daha??')

# for mnv in manav:
#     if len(mnv) > 5:
#         print(f'Ooo ne guzel! {mnv}')
#     elif mnv[0] == 'm':
#         print(f'Bayiliriimmm!! {mnv}')
#     elif mnv[0] == 'e':
#         print(f'Hadi bakalim: {mnv}')
#     else:
#         print(f'Hepsi ayri sulu ayri guzel: {mnv}')
# # 3

# syskoner = ['maria', 'joseph', 'ali', 'ahmet', 'bedir', 'nilgun']
# if len(syskoner) > 3:
#     print('Vad kul')

# for sys in syskoner:
#     if sys[0] == 'j':
#         print(f'De ar tvillingar: {sys}')
#     elif sys[0] == 'b':
#         print(f'Han ar stor bror: {sys}')
#     elif sys[0] == 'n':
#         print(f'Hon ar gift: {sys}')
#     else:
#         print(f'De ar jettefina syskoner: {sys}')

# # 4 

# colors = ['red', 'yellow', 'blue', 'purple', 'black']
# if len(colors) != 5:
#     print('Good!')

# for x in colors:
#     if x[0] in 'r':
#         print(f"I don't like this color: {x}")
#     elif x[0] in 'b':
#         print(f"Yes, it's my favorite color: {x}")
#     elif x[0] == 'p':
#         print(f"It's so boring: {x}")
#     else:
#         print(f'Just color: {x}')

# 0

# Make a list of names that includes at least four people.
# Write an if test that prints a message about the room being crowded, 
# if there are more than three people in your list.
# Modify your list so that there are only two people in it. 
# Use one of the methods for removing people from the list, don't just redefine the list.
# Run your if test again. There should be no output this time, 
# because there are less than three people in the list.
# Bonus: Store your if test in a function called something like crowd_test.

# def crowd_test(f):
#     if len(f) > 3:
#         print('Amma kalabalik!!')
    
# f = ['ayse', 'sadik', 'bedir', 'nilgun']
# crowd_test(f)

# f.pop()
# f.pop()

# crowd_test(f)

# Q1
# Topic: If-Else / For-Loop
# Points: 5
# -----------------------------------------------------------------------------
# o Write a program that asks the user to enter a number.
# o If the number is greater than 10, print "The number is greater than 10".
# o If the number is less than or equal to 10, print "The number is less than or equal to 10".



# def enter_number(a):
#     input = 'Enter a number: ' + str(a)

#     for i in a:
#         if (i > 10):
#             print(f"The number is greater than 10 {i}")
#         else:
#             print(f"The number is less than or equal to 10 {i}")
# enter_number(10)
# Q2
# Topic: If-Else / For-Loop / Lists / Functions
# Points: 20
# -----------------------------------------------------------------------------
# o Jim is in a forest. It's been quite some time he hasn't eaten anything. He knows that he will get hungry soon. He knows that this side of the forest is full of delicious mushrooms. But he also is not good distinguishing poisonous mushrooms from delicious mushrooms.
# o Every mushroom in the forest has a code on it, a string of letters. Luckily, he has a list of codes, if a mushroom includes any of these codes in it's code, then it is poisonous. He needs to however check the mushrooms quickly since he doesn't have much time left. We are going to write a program that will check which mushrooms are poisonous and which are not. And count how many mushrooms Jim can eat.
# o The function is_poisonous takes a mushroom code as an argument and returns True if the mushroom is poisonous and False if it is not.
# o The function count_poisonous takes a list of mushroom codes and returns the number of poisonous mushrooms in the list.
# Sample Input:
# poisonous_codes = ['cod', 'arpe', 'xxyt', 'acr', 'bcd', 'xz']
# forest_mushrooms = ['htrcd', 'tarpes, 'xxytr', 'ceaar', 'vvbctd', vsxz', 'accr', 'ccod', 'ttyt', 'garxxytacr', 'ccd', 'xz']
# Sample Output:
# The forest contains: 12 mushrooms
# Number of poisonous mushrooms: 6
# Number of edible mushrooms: 6



# # Q3
# # Topic: If-Else / Functions
# # Points: 5
# # -----------------------------------------------------------------------------
# # o Write a function that takes the temprature as an argument and prints if user should go outside or not, 
# # and how the weather is. Use at least 3 different if-else statements.
# # o Make up your own loagic about the weather.
# # Sample Input:
# # temprature = -35
# # Sample Output:
# # You should not go outside. It is freezing... Damn!

# def temprature(a):
#     print('Temprature: ' + str(a))

#     if(a <= -10):
#         print('You should not go outside. It is freezing... Damn!')
#     elif(a <= 0):
#         print('The weather is okey.')
#     else:
#         print('The weather is fine.')
        
# temprature(-3)
# temprature(0)
# temprature(10)

# # Q4
# # Topic: If-Else / Functions / Lists
# # Points: 5
# # -----------------------------------------------------------------------------
# # o Write a function that takes a list of numbers as an argument and returns the largest number in the list.
# # o The function should return None if the list is empty.
# # Sample Input:
# # numbers = [1, 2, 3, 4, 5]
# # Sample Output:
# # 5

# def numbers(a):
#     a.sort()
#     print('Largest element is: ', a[-1])

# num = [4,5,6,7,8,9]
# numbers(num)

# # Q5
# # Topic: If-Else / Functions / ?
# # Points: 10
# # -----------------------------------------------------------------------------
# # o Write a function that takes hours as argument (as a float) and converts it to hours, minutes and seconds and prints it.
# # Sample Input:
# # hours = 1.53
# # Sample Output:
# # 1 hour 31 minutes and 48 seconds


# saniye1=int(input("Saat kac: "))
# def dakikasaniye(san):
#     if san<60:
#         print("0 dakika",san,"saniye")
#     elif san>=60:
       
#         dak=int(san//60)
#         cevir=dak*60
#         kalansaniye=san-cevir
#         print(dak,"dakika",kalansaniye,"saniye")
# def saatim(saniye):
#     if saniye<3600:
#         dakikasaniye(saniye)
#     elif saniye>=3600:
#         saat=int(saniye//3600)
#         saat2=int(saat*3600)
#         kalan_saniye=int(saniye-saat2)
#         print(saat,"saat",end=" ")
#         dakikasaniye(kalan_saniye)  
# saatim(dakikasaniye)

# Q6
# Topic: If-Else / Functions / Lists
# Points: 5
# -----------------------------------------------------------------------------
# o Write a function that converts a list of digits into a list of thier names.
# o The function should return None if the list is empty.
# Sample Input:
# numbers = [1, 2, 3, 4, 5]
# Sample Output:
# ['one', 'two', 'three', 'four', 'five']

# Q7
# Topic: If-Else / Functions / ? / ?
# Points: 5
# -----------------------------------------------------------------------------
# o Write a function that takes in a string. The function should return True if the string is a palindrome and False if it is not.
# o A palindrome is a string that is the same forwards and backwards.
# o The function should return None if the string is empty.
# Sample Input:
# string = "racecar"
# Sample Output:
# True

def palindrome(x):
    return x == x[::-1]

x = 'nilgun'
ans = palindrome(x)

x = 'halah'
ans = palindrome(x)

if ans:
    print('True')
else:
    print('False')