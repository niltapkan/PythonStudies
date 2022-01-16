# # Dictionaries
# # {key: value}
# # dict = {
# #   key1: value1,
# #   key2: value2,
# #   key3: value3
# # }
# fruits = {
#     'watermelon': 'A delicious, green miracle!',
#     'strawberry': 'Little red drops from heaven!',
#     'cucumber': 'really?'
# }

# dictionary = {
#     'example': 'a thing characteristic of its kind or illustrating a general rule.',
#     'joy': 'a feeling of great pleasure and happiness.'
# }

# print(f'Watermelon is ' + fruits['watermelon'])

# # for key, value in dictionary.item():
# #   access the key-value pairs here

# # for key in dictionary.key():
# #   access the keys only

# # for value in dictionary.value():

# fruits['banana'] = 'yellow long and dry'

# print(fruits.keys())

# # Modify
# fruits['banana'] = fruits['banana'] + 'but i love it'

# print(fruits['banana'])

# # remove a pair
# del fruits['banana']

# print(fruits.keys())

# # modify a key
#     # recreate(copy) the element pair
#     # remove the old one

# fruits['tomato'] = fruits['cucumber']
# del fruits['cucumber']

# print(fruits.keys())

# # ls = [x,y,z]
# # x <- [1,2,3]
# # y <- [4,5,6]
# # z <- [7,8,9]

# ls = [  [1,2,3],
#         [4,5,6],
#         [7,8,9]
#     ]
# print(ls[1][1])

# numbers = {
#     'odd': [1,3,5,7,9],
#     'even': [0,2,4,6,8]
# }

# print(numbers['odd'][0]) #odd anahtarinin icinde 1 e ulasmak icin bunu yapiyoruz.

# # Default args
# def greetings(name='everyone'):
#     print(f'Hello {name}!')

# greetings()
# greetings('Bedir')

# # Pos args
# def describe_person(first_name, last_name, age):
#     print(f'First name: {first_name}')
#     print(f'Last name: {last_name}')
#     print(f'Age : {age}')

# describe_person('Bedir', 'Tapkan', 25)

# class Rocket():
#     def __init__(self):
#         self.x = 0
#         self.y = 0
# Fleet = [Rocket() for i in range(5)]
# print(Fleet)

# Classes and Instances - Python Nesnel Tabanli Programlama 

# class Personel:  #Bir sinif olusturmus olduk
#     #pass  #Bir mola alalim bi bakalim neler olacak bu sinifta ayrintili yazalim demis olduk.
#     def __init__(self, name, surname, loan):   # 'self' nesneleri ifade ediyor. selften sonra yazdiklarimizi(bunlara argumanlar diyoruz) o nesnede belirt demek istiyoruz.
#         self.name = name.title()   #Bunlar NESNE DEGISKENLERI-INSTANCE VERIABLES olarak geciyor.
#         self.surname = surname.upper()
#         self.loan = loan
#         self.email = f'{name.lower()}{surname.lower()}@work.com'
#     def name_surname(self):
#         return f'{self.name} {self.surname}'

# per_1 = Personel(name= 'Joseph', surname='Bergstrom', loan= 40000)
# per_2 = Personel('Maria', 'Bergstrom', 50000)  # Tek tek veriable isimlerini yazmaya gerek yok. Osira ile yazsanda olur.

# print(per_1.name_surname())
# print(per_1.name)
# print(per_2.loan)
# print(per_2.surname)
# print(per_1.email)
# # print(Personel)
# # print(per_1)
# # print(per_2)

# per_1.name = 'Joseph'
# per_1.surname = 'Bergstrom'
# per_1.email = 'josephb@gmail.com'

# per_2.name = 'Maria'
# per_2.surname = 'Bergstrom'
# per_2.email = 'mariab@gmail.com'

# print(per_2.email)
# print(per_1.name)

# class Ogrenciler:
#     def __init__(self, isim, soyisim, okul_no):
#         self.isim = isim.title()
#         self.soyisim = soyisim.upper()
#         self.okul_no = okul_no
#         self.email = f'{isim.lower()}{soyisim.lower()}.{okul_no}@okul.com'

# ogr_1 = Ogrenciler('Ali', 'Murtaza', 78)

# print(ogr_1.email)

# class animal:
#     def __init__(self, animal_name, color, sahibi):
#         self.animal_name = animal_name.title()
#         self.color = color
#         self.sahibi = sahibi.title()
#     def sahib(self):
#         return f'{self.animal_name}={self.sahibi}'

# an1 = animal('Cat', 'White', 'Nilgun')
# an2 = animal('Dog', 'Brown', 'Abdullah')

# print(an1.sahib())
# print(an2.sahib())

# class car:
#     def __init__(self, model, marke, price, engine, year, color):
#         self.model = model.title()
#         self.marke = marke.title()
#         self.price = price
#         self.engine = engine
#         self.year = year
#         self.color = color
#     def feature(self):
#         return f'{self.model.title()} -> {self.marke.title()}'

# car1 = car('civic','honda',20000, 1.6, 2016, 'white') 

# car2 = car('ibiza', 'seat', 14000, 1.4, 2006, 'red')

# print(car1.feature())
# print(car2.engine)

# class personel:
#     personel_sayisi = 0
#     zam_orani = 1.05

#     def __init__(self, isim, soyisim, maas):
#         self.isim = isim.title()
#         self.soyisim = soyisim.title()
#         self.maas = maas
#         self.epost = f'{isim.lower()}.{soyisim.lower()}@karem.com'

#         personel.personel_sayisi += 1

#     def tam_isim(self):
#         return f'{self.isim.title()} {self.soyisim.title()}'

#     def zam_uygula(self):
#         self.maas = int(self.maas * self.zam_orani)

# per1 = personel('Ali', 'Veli', 200000)
# per2 = personel('Tarik', 'Ali', 30000)

# print(personel.personel_sayisi)
# print(per1.zam_orani)
# print(per1.zam_uygula)

from animals import Animal
class Fish(Animal):
    def __init__(self, ):
        super().__init__()