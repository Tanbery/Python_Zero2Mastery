#list, set, dict

mylist0 = []
for ch in 'hello':
    mylist0.append(ch)
print('List0:', mylist0)

mylist1 = [ch for ch in 'hello']
mylist2 = [num for num in range(0,100)]
mylist3 = [num**2 for num in range(0,100)]
mylist4 = [num**2 for num in range(0,100) if num % 2 == 0]

print('List1:', mylist1)
print('List2:', mylist2)
print('List3:', mylist3)
print('List4:', mylist4)

myset1 = {ch        for ch  in 'hello'}
myset2 = {num       for num in range(0,100)}
myset3 = {num**2    for num in range(0,100)}
myset4 = {num**2    for num in range(0,100) if num % 2 == 0}

print('Set1:', sorted(myset1))
print('Set2:', sorted(myset2))
print('Set3:', sorted(myset3))
print('Set4:', sorted(myset4))

simple_dict = {
    "a":1,
    "b":2
    }
myDict1 = {k:v**2 for k,v in simple_dict.items() if v%2 ==0}
myDict2 = {num:num*2 for num in range(0,100)}
#myDict3 = {num**2 for num in range(0,100)}
#myDict4 = {num**2 for num in range(0,100) if num % 2 == 0}

print('Dict1:', myDict1)
print('Disct2:', myDict2)
#print('Disct3:', myDict3)
#print('Disct4:', myDict4)


orgList =['a','b','c','b','d','m','n','n']
dubList = list({ch for ch in orgList if orgList.count(ch)>1})
print("Orginal List:", orgList)
print("Dublicates  :", dubList)