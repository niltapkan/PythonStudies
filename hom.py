# 1
for i in range(1, 11):
    print(i)

print('\n')

# 2
for i in range(1,10):
    for j in range (1,i):
        print(j, end='')

    print('\n')

# 3

# num = input("enter a positive integer number:")
# for i in range(0, int(num)):
#     print(f'{num} +{i} = {num}')

#     num = int(num) + i 

# 4

# num = input('enter a number')
# for i in range(1,11):
#     print(f'{i}*{num} = {i*int(num)}')


# 5

for i in range(11):
   print(i)

# 6
		
# num = input('enter a number')
# count = 0
# for i in range(len(num)):
#     count +=1
# print(count)

print('\n')
# 7

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print('\n')

# 8
ls2 = [1,2,3,4,5,5,6,7,8]
a = len(ls2)
ls3 = []
for i in range(a-1,-1,-1):
    ls3.append(ls2[i])
print('ls3:', ls3)

# 9

for i in range (10,0,-1):
    print(-i)

print('\n')

# 10

music = []

music.append('a')
music.append('f')
music.append('c')

for i, m in enumerate(music):
    print(str(i + 1) + '-' + m.title())

print('\n')

# 11

for num in range(3, 45):
    if num > 1 :
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

print('\n')

# 12

n1 = 0
n2 = 1

for count in range(11):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3

print('\n')

# 13

# n = int(input(8))
# sum = 1
# for i in range (1, n+1):
#     sum= sum*i
# print('!' + str(n), '=', sum)

# print('\n')

# 14 

for i in range(1,100):
    for j in range (1,i):
        print(j, end='')

    print('\n')

