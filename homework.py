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

# For Loops

# Syntax

# 'in' icinde var mi kontrol ediyoruz. 
# 'for' kendinden sonra bir degisken gelir. 
# sonrasinda 'in' gelerek degiskeni kontrol eder.

for x in ls2:
    print(x + " it's simple.")

ls3 = [(1,2),(3,4),(5,6)]
for x,y in ls3:
    print(x,y)
# Bu sekilde ls3 dekileri x ve y degerlerine atayabiliriz.

playlist = {                     # dictinary oluyor bu.
    "sezen" : "kacin kurasi",
    "tarkan" : "kuzu kuzu",
    "mustafa" : "araba" 
    }
for artist in playlist.keys(): # keys bastaki elemani etkiler
    print(artist)

for artist in playlist.values(): # values ikinci elemanlari etkiler
    print(artist)

for artist, sing in playlist.items(): # items hepsini karsilikli cikarir.
    print(artist, sing)

# Enumerate - Siralama

grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item) # Bu sekilde listedeki her bir elemanin sirasini gormus oluyoruz.

# Peki bunu duzenli halde nasil yazariz?

for count, item in enumerate(grocery):
  print(count, item)

# Eger kendim verdigim bir sayidan saymasini baslatmak istersem.

for count, item in enumerate(grocery,10):
    print(count, item)



# Range
'''
range kelimesi İngilizcede ‘aralık’ anlamına gelir. 
Biz Python’da range() fonksiyonunu belli bir aralıkta
bulunan sayıları göstermek için kullanıyoruz.

'''
print('\n')

for i in range(0,10):
    print(i)

'''
range() fonksiyonu iki parametre alıyor. 
Ama aslında bu fonksiyonun üçüncü bir parametresi daha vardır.

range(ilk_sayı, son_sayı, atlama_değeri)

'''
print('\n')

for i in range(0, 10, 2):
    print(i)

print('\n')

print(range(len(grocery))) # Bu sekilde yazilirsa ciktisi
# range(0,3) cikar. range yazisini gizlemek ve 0 1 2 seklinde
# cikmasi icin '*' seklinde yazmaliyiz.

print('\n')

print(*range(len(grocery)))
# len() -> Bize verinin kac karakterli oldugunu gosterir. Uzunluk olcer.

# Common Op.

# Modify - Veri yerine baska bi sey eklersin.

print('\n')

ls4 = ['elma', 'armut', 'portakal']
ls4[1] = 'mandalina'
print(ls4)

# Find
# index kullaniyoruz.
print('\n')

print(ls4.index('elma')) # verinin kacinci sirada oldugunu bildirir.
#print(ls4.index('apple')) # ValueError: 'microsoft' is not in list.

# If exists - dogru mu yanlis mi diye bakiyoruz.

print('\n')

print('microsoft' in ls4)
print('portakal' in ls4)

# Appending - listeye eklemek icin kullaniyoruz.

print('\n')

ls4.append('microsoft')
print(ls4)

# Inserting - yine eklemek icin kullaniriz ama belli bir yere.

print('\n')

ls4.insert(2, 'DeepMind')
print(ls4)

print('\n')

names = []

names.append('nilgun')
names.append('abdullah')
names.append('lina')

for i, n in enumerate(names):
    print(str(i + 1) + '-' + n.title()) # YAZILISI UNUTMA!!

# Remove #girdigin siradaki elemani siler.

print('\n')

nums = [1, 2, 3, 4]
del nums [0]
print(nums)

print('\n')

nums.remove(2)
print(nums)

# Slicing

print('\n')

nums = [1,2,3,4,5]
print(nums[0: 3])
print(nums[::-2])
print(nums [-1:0:-1])

print('\n')

# Copy

copy_nums = nums[:] # Bu sekilde orjinali kopyalamis oluyoruz. 
#ama orjinal dosyanin aynisi degil yeni dosya oluyor.
#eger orjinal degisirse kopya degismez.
copy_nums_wrong = nums
nums[0] = 2
print(nums)
print(copy_nums)
print(copy_nums_wrong)

# Range

# range (start, end, step)

print('\n')

for a in range(1, 33, 12 ):
    print(a)

# Nums - listeleyerek yazar

print('\n')

nums = list(range(1, 33, 12 ))
print(nums)

# min, max, sum

print('\n')

ages = [23, 25, 35, 18, 45]

youngest = min(ages)
oldest = max(ages)
total_age = sum(ages)

print(youngest, oldest, total_age)