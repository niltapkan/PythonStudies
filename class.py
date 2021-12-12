# # Split

# # split() yöntemi, 
# # belirtilen ayırıcıda bir dizeyi ayırır ve bir dize listesine döndürür.

# text = 'Python is a fun programming language'

# # split the text from space
# print(text.split(' '))

# # Output: ['Python', 'is', 'a', 'fun', 'programming', 'language']

# text= 'Love thy neighbor'
# # splits at space
# print(text.split())
# # Output: ['Love', 'thy', 'neighbor']

# grocery = 'Milk, Chicken, Bread'
# # splits at ','
# print(grocery.split(', '))
# # Output: ['Milk', 'Chicken', 'Bread']

# # Splits at ':'
# print(grocery.split(':'))
# # Output: ['Milk, Chicken, Bread']

# print('My favoriate drink is' + ' ' + grocery.split(',')[0])

# # Tuples
# # immutabla - never can change
# colors = ('red', 'blue', 'green')
# print(colors[0])
# print('\n')
# for color in colors:
#     print(color)

# # colors[0] = 'red' 
# # # Output: TypeError: 'tuple' object does not support item assignment

# #colors.append( 'purble')
# # # Output: AttributeError: 'tuple' object has no attribute 'append'

# #colors.pop()
# # # Output: AttributeError: 'tuple' object has no attribute 'pop'

# # String formating with numbers

# num = 23
# print('Hi '  + str(num))

# print('Hi there beatiful number %d.' % num)

# ls = [7,13,19]
# print('Some of the amazing prime numbers %d, %d, and %d.' % (ls[0], ls[1], ls[2]))

# # %d tam bir sayi icin yer tutucu. - int  
# # %s bir dize icin yer tutucudur. - string
# # %f kesirli sayilar icin. - floats
# name = 'Nilgun'
# number = 26
# ant = 3.4
# print('%s %d %f' % (name, number, ant) ) # '%' aralarina bunu koymadan calismaz.
# # Neyi atayacagini belirliyor.

# print('A float: %.2f' % 3.4) #%.2f noktadan sonra ne kadar sayi olmasini istiyorsak.

# print('\n')

# float_number = 3.0
# print(f'A float: {float_number}, {num}') # dalgali parantez 
# #icindekiler string olmak zorunda degil.

# print('some of the amazing prime numbers are {},{}, and {}.'.format (ls[0], ls[1], ls[2]))

# # Variable types
# # String

# # Int
# a = 2

# # Float
# f = 3.2

# # Bool - dogru yanlis olduguna bakar.
# # True and False
# val = True
# val = False

# # Basic math operators
# a = 3 + 2
# a = 3 - 2
# a = 4 * 2 
# a = 5 / 2
# a = 5 // 2
# a = 5 % 2
# a = 5 ** 2

# # FUNCTIONS

# # Kendi fonksiyonumu olusturmak icin kullaniyoruz.
# #def function_name(arguments):
#     #whatever the action we need
# # Biz 'def' ile bir fonksiyon taniplayip 
# #onun alanindan cikinca artik o fonksiyonu kullanilabilir hale geliyor.

# # function_name(arguments):
# print('You are an amazing person Alliq')
# print('We are appriciating yor existence ...')
# print('Please spend more time with us.')
# print('To enroll, click the button below!')

# print('You are an amazing person Nilgun')
# print('We are appriciating yor existence ...')
# print('Please spend more time with us.')
# print('To enroll, click the button below!')

# print('You are an amazing person Tarik')
# print('We are appriciating yor existence ...')
# print('Please spend more time with us.')
# print('To enroll, click the button below!')

# print('You are an amazing person Jonas')
# print('We are appriciating yor existence ...')
# print('Please spend more time with us.')
# print('To enroll, click the button below!')

# print('You are an amazing person Bedir')
# print('We are appriciating yor existence ...')
# print('Please spend more time with us.')
# print('To enroll, click the button below!')
# #surekli bir tekra var bunu tek bir isimde toplayacagiz.

# def ad_run(name):
#     #print('You are an amazing person Bedir') # Bu sekilde isim yazili olursa butun ciktilar bedir diye gelir.
#     print(f'You are an amazing person {name}') # bu sekilde nereye yazacagini bilir.
#     print('We are appriciating yor existence ...')
#     print('Please spend more time with us.')
#     print('To enroll, click the button below!')

# ad_run('Nilgun')
# ad_run('Bedir')
# ad_run('Tarik')
# ad_run('Jonas')
# ad_run('Diana')

# emails = ['ea@gmail.com', 'as@gmail.com', 'lk@gmail.com', 'ok@gmail.com']

# message = 'Students must bring a pen!'
# for email in emails:
#     print(f'Sent to: {email}')
#     print(f'Message: {message}')

# message = 'Also an eraser please...'
# for email in emails:
#     print(f'Sent to: {email}')
#     print(f'Message: {message}')

# new_emails = emails[:2]
# message = 'No pen, meant pencil!'
# for email in emails:
#     print(f'Sent to: {email}')
#     print(f'Message: {message}') # bu sekilde yine cok tekrr ve uzun bir islem var,
    # bunu kisaltalim.

def email_students(message, emails):
    for email in emails:
        print(f'Sent to: {email}')
        print(f'Message: {message}')
    
emails = ['ea@gmail.com', 'as@gmail.com', 'lk@gmail.com', 'ok@gmail.com']

message = 'Students must bring a pen!'
email_students(message, emails)

message = 'Also an eraser please...'
email_students(message, emails)

message = 'No pen, meant pencil!'
email_students(message, emails[:2])

# def get_number_of_words(sentence):
#     ls = sentence.split(' ')
#     return len(ls) # 'return' le degeri geri al diyoruz.
#     #(bulunan degerin geri gonderilmesi) Returnden sonra fonksiyon biter. kod calismaz

# message = 'The world is an amazing place!'
# lenght = get_number_of_words(message)
# print(lenght)

# def double(a):
#     a*2
# def kare(b):
#     return b*b
# def toplam(c):
#     return c+3

# print(toplam(kare(double(2))))
