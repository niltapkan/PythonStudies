#Variables

from typing import Match


lang = "swedish"
print(lang)

# Naming Rules
#Can : Letters, Numbers, Underscores

lang = "swedish2016"

# Can't: 
# - Start w numbers 
# Ex: 2016swedish
# - No spaces
# Ex: 2016 swedish
# - No keywords
'''
sadece if , int,.. 
kullanamazsin cunku python da bunlar 
anahtar kelime. ama int1,if_our,.. 
yazabilirsin. Bunlar valiebles.

'''

# Strings

lang = "swedish2016"
print(type(lang)) #Bu sekilde yazarsak type ogrenilmis olur.

# Functions

lang = "SweDiSh"
print(lang.lower()) #Tum harfler kucuk
print(lang.title()) #Bas harfler buyuk
print(lang.upper()) #Tum harfler buyuk

# String concatenation

lang1 = "swedish"
lang2 = "finnish"

langg = lang1 + ' ' + lang2

print(lang1 + ' ' + lang2)
print(langg)

# Whitespace
print("I you")
# \t - tab ,ikili bosuk olusturacak 
print("I\tyou")
# \t - t is never shown!
# \n - new line, alt satira yazacak ikinci kelimeyi.
print("I\nyou")

# Stripping Whitespaces
lek1 = '    2 Match 3      '
lek2 = ' 4 Art 5       '
lek = lek1 + lek2

print(lek1.lstrip()+lek2)
print(lek1.rstrip()+lek2)
print(lek1.strip()+lek2)

print(lek1.lstrip().rstrip()+lek2)

print(lek + '-') #ayni sekilde yazdirir.

# Number
# Integer

print(9+2)
print(5-6)
print(3*4)
print(2/1)

#power(sayinin ussunu alir)
print(6**5)

calc = 3 / 2 - 1 + 19
print(calc)

# Floating-point numbers
print(0.1 + 0.1)




