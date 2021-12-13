
# # IF - ELSE 
# # if , else ve elif terimleriyle mantıksal ifadeleri 
# # kullanarak bir durumun koşulu sağlaması durumunda 
# # çalışmasını gerçekleştirebiliriz.
# #Condition checher 
# # If condition:
# #    code to run if True
# # elit another condition:         # Programımızda yeri geldiğinde birden fazla durumu kontrol etmek durumunda kalabiliriz. 
# # Bunun içinde Python programlama dilinde elif terimi devreye girer.
# #   code to run if another condition is True
# # else:                         #Eğer if koşulunun gerçekleşmediği durumda başka 
# # bir durumun gerçekleşmesini istiyorsak bunu else terimi ile gerçekleştirebiliriz.
# #   code to run if none were true

# # condition > true / false
# desserts = ['ice cream', 'chocolate', 'strawberry']
# favorite_dessert = 'ice cream'

# for dessert in desserts:
#     if dessert == favorite_dessert:
#         print(f'{dessert} is my favorite !!')
#     else:
#         print(f'{dessert} is not the best...')
    
# # Logical Tests
# # Koşul durumlarında == , != , < , <= , > , >= ifadelerini kullanabilirsiniz.
# # a == b -> if a is equal to b (value)
# # a != b -> if a is not equal to b (value)
# # a > b
# # a >= b
# # a < b 
# # a <= b 
# # a in ls
# print(5 == 5)
# print(6 == 5)
# print(6 != 5)
# print(3 < 3)
# print(3 >= 3)

# print(3 in [4, 5])
# print('a' in 'car')

# print('Cat'=='cat')
# print('Cat'.lower() == 'cat')

# Exercise
# 0:
#   - Write a program that consists of at least ten lines, 
# each of which has a logical statement on it. The output of your program should be 5 Trues and 5 Falses.

# students = ['bedir', 'nilgun', 'tarik', 'jonas', 'khkuj']
# if len(students) > 4 :
#     print('The class is big enough')

# for student in students:
#     if len(student) > 5:
#         print(f'The letter here are too crowded: {student} ')
#     elif student[0] == 'j':
#         print(f'Well, who do we have here! Such an honor: {student}')
#     else:
#         print(f'Well this one is just perfect: {student}')

# Logical Tests
# 