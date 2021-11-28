# Lists and Tuples

#Lists
students = ['tarik','diana','yusuf','nilgun','yunus']

# Naming and Defining (genelde cogul yazariz liste adini)
# variable_name = [items]
colors = ['r','g','a']

# Accessing elements
# 0, 1, 2, 3, ..... n 
'''
(pythonda sifirla baslar her zaman.
ilk element her zaman 0 olarak kabul edilir)

'''
#ith element -> name_of_the_var[i]
# the_color = colors[0]
# print(the_color)

# print(colors[1])

# access reverse
# print(colors[-1])

#no no no
#print(colors[3]) / print(colors[-3]) / print(colors[-4])
# Inde

# loops in Lists
names = ['bdr', 'trk', 'dna', 'nl', 'huz', 'yus']

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])

#for name in names: #  verileri alt alta yazmamiza yardimci olur.
    #print(name)    # liste adini degistirmemize yarar.

# syntax
# for var_name in list_name:
# -> whatever code to run

# for x in names:
#     print(x + ' is not that great') # bastaki bosluk olmali.
#     print('And' + x + ' knows it!') # bastaki bosluk olmali hepsinde yazdirmak icin.
# print("That's all a joke!")

# Enumerate
tech_comps = ['microsoft', 'apple', 'google']

#for i, comp in enumerate(tech_comps):
    #print(str(i + 1) + '-' + comp.title()) # - bu isaret icin str yada int yazmaliyiz.
    # print((i + 1) + ' ' + comp.tittle())
    #print((i + 1), comp.title())

# for i in range(len(tech_comps)):
#     print(tech_comps[i])

#print(*range(len(tech_comps))) # '*' bu isaret range yazisini gizler.
#range yazisi verinin siralamasini yapar.

# l1 = ['1', '2', '3']

# for l11 in l1:
#      print(l11)
# l2 = ['one', 'two', 'three']
# for i in range(len(l1)):
#     print(l1[i], l2[i])

# Common Op.
# Modify - Veri yerine baska bi sey eklersin.
# tech_comps = ['microsoft', 'apple', 'google']
# tech_comps[0] = 'amazon'

# print(tech_comps)

# Find
#print(tech_comps.index('apple')) # verinin kacinci sirada oldugunu bildirir.
# print(tech_comps.index('microsoft'))
# ValueError: 'microsoft' is not in list

# If exists - dogru mu yanlis mi diye bakiyoruz.
# print('microsoft' in tech_comps)
# print('apple' in tech_comps)

# Appending - listeye eklemek icin kullaniyoruz.
# tech_comps.append('microsoft')
# print(tech_comps)

# Inserting - yine eklemek icin kullaniriz ama belli bir yere.
# tech_comps.insert(2, 'DeepMind')
# print(tech_comps)

# social_medias = []

# add comps
# social_medias.append('facebook')
# social_medias.append('instagram')
# social_medias.append('whatsapp')

# for i, sm in enumerate(social_medias):
#     print(str(i + 1) + '-' + sm.title())

# sorting a list - listeyi tersten yazar
# tech_comps.sort()
# for i, tc in enumerate(tech_comps):
#     print(str(i + 1) + '-' + tc.title())

# reverse sort
# tech_comps.sort(reverse=True) # bir bu sekilde yapilabilir.
# for tc in tech_comps:
#     print(tc)
# print(tech_comps[::-1]) # bir de bu sekilde yapilabilir


# sort vs sorted
# tech_comps_sorted = sorted(tech_comps)
# print(tech_comps)
# print(tech_comps_sorted)

ls = ['1', '2', '3', '4']
# ls.sort(reverse= True)
# print(ls)
# print(ls[::-1])

# Numerical sorting
# nums = [1, 2, 3, 4]
# print(sorted(nums))
# print(sorted(nums,reverse=True))
# nums.reverse()
# print(nums)

# Lenght
# lenght = len(nums)
# print(lenght)

# Remove #girdigin siradaki elemani siler.
nums = [1, 2, 3, 4]
del nums [0]
print(nums)

# by val
nums.remove(2)
print(nums)

nums = [ 2, 3, 2, 4]
nums.remove(2)
print(nums)

#pop - listenin sonundakini siler
# nums = [1,2,3,4,5]
# last = nums.pop() #last koymasanda calisir.
# print(nums)
# print(last)

# one = nums.pop(0)
# print(nums)
# print(one)

# Slicing
# var_name[sart_idx:stop_index:step_size]
# [0:end:1]
nums = [1,2,3,4,5]
print(nums[0: 3])
print(nums[::-2])
#print(nums [-1:0:-1])

copy_nums = nums[:] # Bu sekilde orjinali kopyalamis oluyoruz. 
#ama orjinal dosyanin aynisi degil yeni dosya oluyor.
#eger orjinal degisirse kopya degismez.
copy_nums_wrong = nums
nums[0] = 2
print(nums)
print(copy_nums)
print(copy_nums_wrong)

# range
# range (start, end, step)
for n in range(1, 2, 33):
    print(n)

nums = list(range(1, 2, 33))
print(nums)

# min, max, sum
ages = [23, 25, 35, 18, 45]

youngest = min(ages)
oldest = max(ages)
total_age = sum(ages)

print(youngest, oldest, total_age)