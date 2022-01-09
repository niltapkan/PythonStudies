# Dictionaries
# {key: value}
# dict = {
#   key1: value1,
#   key2: value2,
#   key3: value3
# }
fruits = {
    'watermelon': 'A delicious, green miracle!',
    'strawberry': 'Little red drops from heaven!',
    'cucumber': 'really?'
}

dictionary = {
    'example': 'a thing characteristic of its kind or illustrating a general rule.',
    'joy': 'a feeling of great pleasure and happiness.'
}

print(f'Watermelon is ' + fruits['watermelon'])

# for key, value in dictionary.item():
#   access the key-value pairs here

# for key in dictionary.key():
#   access the keys only

# for value in dictionary.value():

fruits['banana'] = 'yellow long and dry'

print(fruits.keys())

# Modify
fruits['banana'] = fruits['banana'] + 'but i love it'

print(fruits['banana'])

# remove a pair
del fruits['banana']

print(fruits.keys())

# modify a key
    # recreate(copy) the element pair
    # remove the old one

fruits['tomato'] = fruits['cucumber']
del fruits['cucumber']

print(fruits.keys())

# ls = [x,y,z]
# x <- [1,2,3]
# y <- [4,5,6]
# z <- [7,8,9]

ls = [  [1,2,3],
        [4,5,6]
        [7,8,9]
    ]
print(ls[1][1])

numbers = {
    'odd': [1,3,5,7,9],
    'even': [0,2,4,6,8]
}

print(numbers['odd'][0]) #odd anahtarinin icinde 1 e ulasmak icin bunu yapiyoruz.

# Default args
def greetings(name='everyone'):
    print(f'Hello {name}!')

greetings()
greetings('Bedir')

# Pos args
def describe_person(first_name, lsat_name, age):
    print(f'First name: {first_name}')
    print(f'Last name: {last_name}')
    print(f'Age : {age}')

describe_person('Bedir', 'Tapkan', 25)
