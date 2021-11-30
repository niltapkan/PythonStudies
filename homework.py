# 46. Vecka

# #Variables

# from typing import Match

# lang = "swedish"
# print(lang)

# # Naming Rules
# #Can : Letters, Numbers, Underscores

# lang = "swedish2016"

# # Can't: 
# # - Start w numbers 
# # Ex: 2016swedish
# # - No spaces
# # Ex: 2016 swedish
# # - No keywords
# '''
# sadece if , int,.. 
# kullanamazsin cunku python da bunlar 
# anahtar kelime. ama int1,if_our,.. 
# yazabilirsin. Bunlar valiebles.

# '''

# # Strings

# lang = "swedish2016"
# print(type(lang)) #Bu sekilde yazarsak type ogrenilmis olur.

# # Functions

# lang = "SweDiSh"
# print(lang.lower()) #Tum harfler kucuk
# print(lang.title()) #Bas harfler buyuk
# print(lang.upper()) #Tum harfler buyuk

# # String concatenation

# lang1 = "swedish"
# lang2 = "finnish"

# langg = lang1 + ' ' + lang2

# print(lang1 + ' ' + lang2)
# print(langg)

# # Whitespace
# print("I you")
# # \t - tab ,ikili bosuk olusturacak 
# print("I\tyou")
# # \t - t is never shown!
# # \n - new line, alt satira yazacak ikinci kelimeyi.
# print("I\nyou")

# # Stripping Whitespaces
# lek1 = '    2 Match 3      '
# lek2 = ' 4 Art 5       '
# lek = lek1 + lek2

# print(lek1.lstrip()+lek2)
# print(lek1.rstrip()+lek2)
# print(lek1.strip()+lek2)

# print(lek1.lstrip().rstrip()+lek2)

# print(lek + '-') #ayni sekilde yazdirir.

# # Number
# # Integer

# print(9+2) # toplama
# print(5-6) # cikarma
# print(3*4) # carpma
# print(2/1) # bolme
# print(4 // 5) # sonucu tam sayi olarak cikarir.
# print(4 % 5) # kalani bize verir.
# print(6**5) # power(sayinin ussunu alir)

# calc = 3 / 2 - 1 + 19
# print(calc)

# # Floating-point numbers
# print(0.1 + 0.1)

# 47. Vecka

# Lists and Tuples

#Lists
# variable_name = [items]
colors = ['red', 'blue', 'yellow', 'black'] 
print(colors)

# Accessing elements - Elemanlara erisim.
# 0, 1, 2, 3, ..... n 
'''
(pythonda sifirla baslar her zaman.
ilk element her zaman 0 olarak kabul edilir)

'''
# Elemani veride bulmak icin;

# 0'dan 1'e kadar olan elemani veri icinde arar.
print(colors[0 : 1]) # koseli parantez olmazsa calismaz!

# Ikinci elemana kadar olanlari cikarir.
print(colors[:3])

# Ikinci elemani veriden atar ve onsuz cikti alir.
print(colors[::2])

# - olarak eleman aratacaksak tersten arar ve sifirdan sayma baslamaz. 
# Yazdigin yere kadar olanlari atar ve o sekilde kalanin ciktisini alir.
print(colors[:-3])

# access reverse - ters erisim
print(colors[-2]) 
'''
Veri kac elemanliysa o kadarlik 
sayi yazip eleman bulabiliriz. 
Aksi takdirde bos cikti alir.
'''

# Loops in Lists

numbers = ['bes', 'alti', 'sekiz', 'on', 'yirmi' ]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3]) 
print(numbers[4])# Bu sekilde tek tek yazmak yerine;

# Verileri alt alta yazmak icin;

for nm in numbers:
    print(nm)

impt_numbers = numbers[0:2]
print(impt_numbers) # Bu sekilde ana listeden ayri bir liste, veri olusturabiliriz.

numbers[3] = 'dort'
print(numbers) # Bu sekilde listedeki elemani degistirbiliriz!

b = 'monday'
# b[0] = 't'
# print(b) # Liste olmadan bu sekilde veriye atama, degisiklik yapamiyoruz.

b = list(b) # Once bu sekilde veriable i listeye donusturuyoruz.
print(b)
b[0] = 't'
print(b) # Daha sonra listede elemanin degistigini goruyoruz. 
# ciktiyi liste sekilde verir. Peki veriable seklinde nasil cikti aliriz?
print(''.join(b)) # Bu sekilde!

ls = ['a', 'b', 'c', 'd']
print(ls)


# Append - Ekleme
ls.append(8) # Listeye eleman eklemek icin kullaniriz.
print(ls)

# Pop - Cikarma
ls.pop(1)
print(ls) 

ls.pop() # Eger bir parametre girilmezse listenin sonundaki elemani cikarir.
print(ls)

a = ls.pop() # 'a' yerine ne yazarsan yaz bu sekilde listede cikarilani verir.
print(a) 

ls1 = [1, 2, 3, 34, 54, 756, 234, 45456, 5778 ]
ls1.sort() # Bu sekilde listenin icini buyukten kucuge siralamis oluruz.
print(ls1)

ls1.sort(reverse=True)
print(ls1) # Bu sekilde buyukten kucuge dogru siralar.

ls2 = ['Ahmet', 'Ayse', 'Betul', 'Yasemin']
ls2.sort() # Bu sekilde bir liste olursa alfabetik siraya gore yapar.
print(ls2)

classes = ['Nilgun','Bedir', 'Tarik', 'Merve']
pasword = ['123', '456', '789', '246']
users = [classes, pasword]
print(users)
print(users[0][0], users[1][0])
print(users[0][1], users[1][1])
print(users[0][2], users[1][2])
print(users[0][3], users[1][3]) # Bu sekilde birbirini eslestirebilirsin listeleri.

# len() -> Bize verinin kac karakterli oldugunu gosterir. Uzunluk olcer.

