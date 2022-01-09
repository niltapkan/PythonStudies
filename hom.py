# # 1
# for i in range(1, 11):
#     print(i)

# print('\n')

# # 2
# for i in range(1,10):
#     for j in range (1,i):
#         print(j, end='')

#     print('\n')

# # 3

# # num = input("enter a positive integer number:")
# # for i in range(0, int(num)):
# #     print(f'{num} +{i} = {num}')

# #     num = int(num) + i 

# # 4

# # num = input('enter a number')
# # for i in range(1,11):
# #     print(f'{i}*{num} = {i*int(num)}')


# # 5

# for i in range(11):
#    print(i)

# # 6
		
# # num = input('enter a number')
# # count = 0
# # for i in range(len(num)):
# #     count +=1
# # print(count)

# print('\n')
# # 7

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print('\n')

# # 8
# ls2 = [1,2,3,4,5,5,6,7,8]
# a = len(ls2)
# ls3 = []
# for i in range(a-1,-1,-1):
#     ls3.append(ls2[i])
# print('ls3:', ls3)

# # 9

# for i in range (10,0,-1):
#     print(-i)

# print('\n')

# # 10

# music = []

# music.append('a')
# music.append('f')
# music.append('c')

# for i, m in enumerate(music):
#     print(str(i + 1) + '-' + m.title())

# print('\n')

# # 11

# for num in range(3, 45):
#     if num > 1 :
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# print('\n')

# # 12

# n1 = 0
# n2 = 1

# for count in range(11):
#     print(n1)
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3

# print('\n')

# # 13

# # n = int(input(8))
# # sum = 1
# # for i in range (1, n+1):
# #     sum= sum*i
# # print('!' + str(n), '=', sum)

# # print('\n')

# # 14 
# num = 1234
# print(str(num)[::-1])

# # 15
# ls = ['B', 'N', 'M']
# print('KArdesler: ')
# for i in range(3):
    # print(ls[i])

# 16

# for i in range(10):
#     print(i ** 3)

# # 17 
# n = 5
# sayi = 0 
# toplam = 0
# for i in range(0, n):
#     sayi = sayi * 10 + 2
#     toplam = toplam + sayi   
# print(toplam)

# # 18
# rows = 5
# def pyramid(rows):
#     for i in range(rows):
#         print(''*(rows - i - 1)+'* '*(i+1))
#     for j in range(rows-1,0,-1):
#         print(''*(rows-j)+'* '*(j))

# pyramid(rows)

# # 19
# n = 5
# for i in range(n-1):
#     for j in range(i, n):
#         print('  ', end='')
#     for j in range(i):
#         print('* ',end='')
#     for j in range(i + 1):
#         print('* ', end='')
#     print()

# for i in range(n):
#     for j in range(i + 1):
#         print('  ', end='')
#     for j in range(i, n-1):
#         print('* ', end='')
#     for j in range(i,n):
#         print('* ',end='')
#     print()

# # 20
# def personal_questions():
#     print('Cat care course')
#     input('Name: ')
#     input('Surname: ')
#     i = int(input('Age: '))
#     if (i >= 12):
#         print('Welcome to Cat care course!')
#     else:
#         print('Not suitable for this age range.')   
# personal_questions()

# Q1

# py = []
# for i in range(1,11):
#     py.append(i+13)
# print(py)

# Q2

# a = "The quick brown fox jumps over the lazy dog."
# b = "My name is Inigo Montoya. You killed my father. Prepare to die."
# c = "Luke, I am your father"

# a1 = [word[0:7] for word in a + b + c]
# print(a1)

# Q3

# a = "A day without sunshine is like, you know, not a day."
# b = "Dreams come true. Without a dream, nothing happens."
# c = "Dry day in a drought."
# e = "Dance or die. The choice is dreadfully simple."

# x = a.find('d')
# print(x)

# Q4
# a = "My cat is my best friend."
# b = "This cat is outrageous."
# c = "We have a cat problem."
# new_a = a.replace('cat', 'dog')
# new_b = b.replace('cat', 'dog')
# new_c = c.replace('cat', 'dog')
# print(new_a)
# print(new_b)
# print(new_c)

# # Q5
# a = 'Nilgun Bedir Tarik Ali Merve Burak '
# slice1 = a[0 : 5]

# slice2 = a[-6 : -1]

# print(slice1)
# print(slice2)

# # Q6

# def sirali(a):
#     A = 0
#     C = 0
#     T = 0
#     G = 0
#     for i in range(0, len(a)):
#         if a[i] == 'A':
#             A += 1
#         if a[i] == 'C':
#             C += 1
#         if a[i] == 'T':
#             T += 1
#         if a[i] == 'G':
#             G += 1
#     return A, C, T, G

# print(sirali("ATGCTTCAGAAAGGTCTTACG."))

# Q7
# Topic: String Manipulation
# An RNA string is a string formed from the alphabet containing 'A', 
# 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed
# RNA string u is formed by replacing all occurrences of 'T' in t with 'U'
# in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.

# source: https://rosalind.info/problems/rna/
from typing import final


t = 'GATGGAACTTGACTACGTAAATT'
u = t.replace('T', 'U')
print(u)

# Q8
# Topic: String Manipulation
# In DNA strings, symbols 'A' and 'T' are complements of each other,
# as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by
# reversing the symbols of s, then taking the complement of each symbol
# (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.

# source: https://rosalind.info/problems/revc/

def reverse_complement(seq):
    listseq = list(seq)
    output = ''
    for base in listseq:
        if base == 'A':
            output += 'C'
        if base == 'T':
            output += 'G'
        if base == 'C':
            output += 'A'
        if base == 'G':
            output += 'T'
    return output
print(reverse_complement('AAAACCCGGT'))

# Q9
# Topic: General
# - Make a list of the most important words you have 
#   learned in programming so far. You should have terms such as list,
# - Make a corresponding list of definitions. Fill your list with 'definition'.
# - Use a for loop to print out each word and its corresponding definition.
# - Maintain this program until you get to the section on Python's Dictionaries.
important_words = ['List', 'String', 'Def', 'for loop', 'while loop', 'if/else']
definition = ['Liste yapilir', 'Degisken tipi', 'Fonksiyon olusturma', 'for dongusu', 'while dongusu', 'sart/kosul']
for i in range(len(important_words)):
    print(important_words[i], '=', definition [i])
 
# # Q10
# # Topic: Functions
# # - Many songs follow a familiar variation of the pattern of verse, 
# #   refrain, verse, refrain. The verses are the parts of the song 
# #   that tell a story - they are not repeated in the song. The refrain
# #   is the part of the song that is repeated throughout the song.
# # - Find the lyrics to a song you like that follows this pattern. 
# #   Write a program that prints out the lyrics to this song, 
# #   using as few lines of Python code as possible.


# # BONUS QUESTIONS
# # ---------------
# # Q1
# # Topic: List Comprehensions
# # Write a program that prints out the first 10 powers of 2.
# for i in range(1, 11):
#     print(2 ** i)

# # Q2
# # Topic: Functions
# # Write a program that takes in a string and prints out the number of
# # times that the string "bob" appears in the given string.
# str = 'bob'
# print(len(str))

# # Q3
# # Topic: Functions
# # Write a program that takes in a string and prints out whether or not
# # the string is a palindrome. A palindrome is a word or phrase that is
# # the same forwards and backwards.
# def palindrome(x):
#     if x == '':
#         return None
#     elif x == x[::-1]:
#         return True
#     else:
#         return False

# print(palindrome(input('Bir palindrome metin giriniz: ')))

# Q4
# Topic: Functions
# Write a program that takes in a string and prints out the number of
# vowels in the string.
string = 'halihazir'
vowels = 'aeiou'
def check_vowels(word):
    counter = 0
    for letter in vowels:
        for letter2 in word:
            if letter == letter2: counter += 1
            else: pass
    print(counter)
check_vowels(string)   


# Q5
# Topic: String Manipulation, Functions
# Write a function that converts a strings letters alternating between
# upper and lower case.

    
# Q6
# Read the Python styling guides summary here; 
#
# Indentation
# - Use 4 spaces for indentation. This is enough space to give
#   your code some visual structure, while leaving room for 
#   multiple indentation levels. There are configuration settings 
#   in most editors to automatically convert tabs to 4 spaces, and 
#   it is a good idea to check this setting. On Geany, this is under 
#   Edit>Preferences>Editor>Indentation; set Width to 4, and Type to 
#   Spaces.

# Line Length
# - Use up to 79 characters per line of code, and 72 characters for comments. 
#   This is a style guideline that some people adhere to and others completely 
#   ignore. This used to relate to a limit on the display size of most monitors. 
#   Now almost every monitor is capable of showing much more than 80 characters 
#   per line. But we often work in terminals, which are not always high-resolution. 
#   We also like to have multiple code files open, next to each other. It turns 
#   out this is still a useful guideline to follow in most cases. There is a 
#   secondary guideline of sticking to 99 characters per line, if you want longer 
#   lines.
# - Many editors have a setting that shows a vertical line that helps you keep 
#   your lines to a certain length. In Geany, you can find this setting under 
#   Edit>Preferences>Editor>Display. Make sure "Long Line Marker" is enabled, 
#   and set "Column" to 79.

# Blank Lines
# - Use single blank lines to break up your code into meaningful blocks. You 
#   have seen this in many examples so far. You can use two blank lines in longer 
#   programs, but don't get excessive with blank lines.

# Comments
# - Use a single space after the pound sign at the beginning of a line. If you 
#   are writing more than one paragraph, use an empty line with a pound sign 
#   between paragraphs.

# Naming Variables
# - Name variables and program files using only lowercase letters, underscores, 
#   and numbers. Python won't complain or throw errors if you use capitalization, 
#   but you will mislead other programmers if you use capital letters in variables 
#   at this point.
# Q1+
# # Topic: If-Else / For-Loop
# # Points: 5
# # -----------------------------------------------------------------------------
# # o Write a program that asks the user to enter a number.
# # o If the number is greater than 10, print "The number is greater than 10".
# # o If the number is less than or equal to 10, print "The number is less than or equal to 10".


# a = int(input('Enter a number: '))
# if (a > 10):
#     print("The number is greater than 10")
# else:
#     print("The number is less than or equal to 10")


# # Q2?
# # Topic: If-Else / For-Loop / Lists / Functions
# # Points: 20
# # -----------------------------------------------------------------------------
# # o Jim is in a forest. It's been quite some time he hasn't eaten anything. He knows that he will get hungry soon. He knows that this side of the forest is full of delicious mushrooms. But he also is not good distinguishing poisonous mushrooms from delicious mushrooms.
# # o Every mushroom in the forest has a code on it, a string of letters. Luckily, he has a list of codes, if a mushroom includes any of these codes in it's code, then it is poisonous. He needs to however check the mushrooms quickly since he doesn't have much time left. We are going to write a program that will check which mushrooms are poisonous and which are not. And count how many mushrooms Jim can eat.
# # o The function is_poisonous takes a mushroom code as an argument and returns True if the mushroom is poisonous and False if it is not.
# # o The function count_poisonous takes a list of mushroom codes and returns the number of poisonous mushrooms in the list.
# # Sample Input:
# poisonous_codes = ['cod', 'arpe', 'xxyt', 'acr', 'bcd', 'xz']
# forest_mushrooms = ['htrcd', 'tarpes', 'xxytr', 'ceaar', 'vvbctd', 'vsxz', 'acr', 'ccod', 'ttyt', 'garxxytacr', 'ccd', 'xz']
# # Sample Output:
# # The forest contains: 12 mushrooms
# # Number of poisonous mushrooms: 6
# # Number of edible mushrooms: 6

def is_poisonous(mushroom, poisonous_codes):
    # mushroom = arpe
    # poisonous_codes = ['cod', 'arpe', 'xxyt', 'acr', 'bcd', 'xz']
    for code in poisonous_codes:
        if code in mushroom:
            return True # poisonous
    return False # non-poisonous


def count_poisionous(mushroom_list, poisonous_codes):
    counter_p = 0
    for mushroom in mushroom_list:
        if is_poisonous(mushroom, poisonous_codes):
            counter_p = counter_p + 1
    return counter_p


poisonous_codes = ['cod', 'arpe', 'xxyt', 'acr', 'bcd', 'xz']
forest_mushrooms = ['htrcd', 'tarpes', 'xxytr', 'ceaar', 'vvbctd', 'vsxz', 'accr', 'ccod', 'ttyt', 'garxxytacr', 'ccd', 'xz']
num_p = count_poisionous(forest_mushrooms, poisonous_codes)
num_m = len(forest_mushrooms)

print(f'Total number of mushrooms:\t{num_m}')
print(f'Number of poisonous:\t\t{num_p}')
print(f'Number of edible:\t\t{num_m - num_p}')

# # Q3+
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
#     a = int(input('Temprature: '))

#     if(a <= -10):
#         print('You should not go outside. It is freezing... Damn!')
#     elif(a <= 0):
#         print('The weather is okay.')
#     else:
#         print('The weather is fine.')
        
# temprature(a = int(input('Temprature: ')))


# # Q4+
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

# # Q5 ...
# # Topic: If-Else / Functions / ?
# # Points: 10
# # -----------------------------------------------------------------------------
# # o Write a function that takes hours as argument (as a float) and converts it to hours, 
# # minutes and seconds and prints it.
# # Sample Input:
# # hours = 1.53
# # Sample Output:
# # 1 hour 31 minutes and 48 seconds

# def hours(a):



# # Q6+
# # Topic: If-Else / Functions / Lists
# # Points: 5
# # -----------------------------------------------------------------------------
# # o Write a function that converts a list of digits into a list of thier names.
# # o The function should return None if the list is empty.
# # Sample Input:
# # numbers = [1, 2, 3, 4, 5]
# # Sample Output:
# # ['one', 'two', 'three', 'four', 'five']

# ls = [0,2,3,6,4,8,1,7,5,9]
# ls1 = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# ls.sort()
# for i in ls:
#     ls[i] = ls1[i]
# print(ls)

# # Q7+
# # Topic: If-Else / Functions / ? / ?
# # Points: 5
# # -----------------------------------------------------------------------------
# # o Write a function that takes in a string. The function should return True if the string is a palindrome and False if it is not.
# # o A palindrome is a string that is the same forwards and backwards.
# # o The function should return None if the string is empty.
# # Sample Input:
# # string = "racecar"
# # Sample Output:zfz
# # True

# def palindrome(x):
#     if x == '':
#         return None
#     elif x == [-1]:
#         return True
#     else:
#         return False

# print(palindrome(x = input()))

# Q8
# Topic: If-Else / For-Loop / Lists / Functions
# Points: 40
# -----------------------------------------------------------------------------
# o We want to create a partial to-do list. We want to be able to add new items to the list, remove items from the list, and mark items as completed. We then want to be able to print the list.
# o Create a function called add_item that takes in a list and a string. The function should add the string to the list.
def add_item(ls):
    item = input("Enter what you wanna add: ")
    ls.append(item) 
todo_list = ['wash car', 'buy groceries', 'pay bills']
add_item(todo_list)
# o Create a function called remove_item that takes in a list and a string. The function should remove the string from the list.
def remove_item(ls):
    item = input("Enter what you wanna remove: ")
    ls.remove(item)   
# o Create a function called mark_completed that takes in a list and a string. The function should mark the string as completed.
def mark_completed(ls):
    item = input()
    ls.
# o Create a function called print_list that takes in a list. The function should print the list.
# Sample Input:
# todo_list = ['wash car', 'buy groceries', 'pay bills']
# Sample Output:
# - wash car
# - buy groceries
# - pay bills
###
# Add an item to the list: 'go to the gym'
# Remove an item from the list: 'pay bills'
# Mark an item as completed: 'wash car'
# Run the program again to see the updated list.
# Sample Output:
# x wash car
# - buy groceries
# - go to the gym
# -----------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
