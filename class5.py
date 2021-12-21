# While Loops
# while condition:
#   run the code as long as condition is statisfied
# health = 5

# while health > 0:
#     print(f'Still fighting..! Health: {health}')

#     health = health -1
# print('You are dead now.')
# Exercise
# Make a variable called strength, and set its initial value to 5.
# Print a message reporting the player's strength.
# Set up a while loop that runs until the player's strength increases to a value such as 10.
# Inside the while loop, print a message that reports the player's current strength.
# Inside the while loop, write a statement that increases the player's strength.
# Outside the while loop, print a message reporting that the player has grown too strong, and that they

# strength = 5
# increase = 1

# while strength != 10:
#     print(f'Your strength is {strength}')
#     strength += increase 
#     print(f'Your strength has increased by {increase}')
# print('You are too strong, you have now leveled up!!!!!!!!!!')

# # Input Taking
# # variable = input('Message')
# # it takes a str
# names = ['bedir']
# another_name = input('A name I should know: ')
# names.append(another_name)
# print(names)

# games = ['as', 'fgh', 'jk', 'kh']
# print(games)
# new_game = input('Yeni oyun: ')
# games.append(new_game)
# print(games)

# # While loops - keep it running
# new_name = ''
# names = []
# while new_name != 'quit':
#     new_name = input('Give me a name (type quit if you want to stop): ')
#     names.append(new_name)
# print(names)
# def play_games():
#     pass
# def display_options():
#     pass
# # While - Menu
# choice = ''

# while choice != 'q':
#     print('[1] Start the game')
#     print('[2] Options')
#     print('[3] Quit')

#     # Ask user
#     choice = input('Please choose an index: ')

#     if choice == '1':
#         play_games()
#     elif choice == '2':
#         display_options()
#     elif choice == 'q':
#         # display a thank you message
#         print(                                        )                                      

# Dictionaries
# l = [3,4]
# l[0]

# dct = {}
# dct = {
#     key: value
# }
# dct = {
#     'bedroom': 'beatiful room', 
#     3: 'hi there'
# }
# print(dct['bedroom'])
# print(dct[3])

# for key, value in dct.items():
#     print(key, ':', value)

#########
# dictionary_name = {
#   key1: value1,
#   key2: value2,   
#   ...
# }

# attributes = {
#     'bedir': 'is tall.'
#     'tarik': 'has dark hair.'
#     'huze': 'wears glasses'
# }
# name = 'bedir'
# print(f'{name} {attributes[name]}')

# for key, value in attributes.items():
#     print(f'{key} {value}') #value: icerdeki anahtar kelimenin karsisindaki.

# Update
# p1 = {
#     'name': 'one plus',
#     'price': 5000
# }
# print(p1)
# p1['price'] = 4000 # Bu sekilde update yapabilirsin icerideki elemandan birine.
# # Diyelim ki eleman eklemek istersen
# p1.update(
#     {
#     'name': 'one plus',
#     'price': 4000,
#     'description': 'good'
#     }
# )
# print(p1)
# p1['color'] = 'white'# Bu sekilde de ekleme yapabilirsin.
# print(p1)
# # Pop - Eleman silmek icin
# p1.pop('name')
# print(p1)

# p1.popitem() # En son ekleneni siler.
# print(p1)

# p1.clear() # bos bir adrese gitmis oluruz.
# print(p1)

p2 = {
    'name': 'one plus6',
    'price': 5000
}

p1 = p2.copy() # p1 i yazmadan p2nin kopyasina esit bir dosya diye gosterbiliriz.
# bu sekilde ana p2 yi degistirmeden p2 dosyasinin kopyasinin p1 oldugunu 
# sonrasinda o dosya icinde degismesi gereken value ler varsa yada eklenmesi
# gereken key ler onlari ekleyebilir, degistirebiliriz.

p1['price'] = 9000

products = [p1, p2, {'name':'oneplus5', 'price':2000}] # product uzerinde 
#dongu kurulabilir.


for p in products:
    # print(p)
    print(p.get('name'))
# meyveler = {
#     'elma': 'en bi sevdigimdir.',
#     'karpuz': 'yazlari ne hos dedigimdir.',
#     'muz': 'Allahim bu nasil bir kurtaricidir.'}

# print(meyveler)
# for i in meyveler.items():
#     print(i)
# for i in meyveler.items():
    # print(i[0] + ' ' + i[1])
# for i,j in meyveler.items():
#     print(i + ' ' + j)
# sinif = {
#     'Birinci sira': 'Nilgun',
#     'Ikinci sira': 'Bedir',
#     'Ucuncu sira': 'Tarik'
# }
# sira = input('Sirayi giriniz:')
# print('{}da: '.format(sira) )
# for i in (sinif[sira]):
#     print(i)
# telefon_rehberi = {
#     'Bedir': '0768598476',
#     'Nilgun': '078653422',
#     'Tarik': ['0998746527', '098876544']
# }
# isim = input('Isim: ')
# for i in (telefon_rehberi[isim]):
#     print(i)

