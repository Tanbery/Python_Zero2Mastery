#for Loops
for item in (1,2,3,4,5,6,7,8):
	print(f'Item is {item}')

print('-------------------------------------')
##iterable: list, dict, tuple, set, string 
##go and check each item one by one in collection
user = {
	 'name':'Golem'
	,'age' : 5006
	,'canSwim': False
}

print('User Items1')
for item in user.items():
	print('\t',item)

print('User Items2')
for key,value in user.items():
	print('\t',key,value)


print('User Keys')
for item in user.keys():
	print('\t',item)

print('User Values')
for item in user.values():
	print('\t',item)

#print('-------------------------------------')
#myList = list(range(1,99))
#total  = 0
#print('Starting sum-up the list')
#for item in myList:
#	print(f'\t{total} + {item} = {total+item}')
#	total+=item
#print(f'Sum-up is finished. Total is {total}')

#print('-------------------------------------')
#for i, char in enumerate(range(101,110)):
#	print(i+1,char)

i = 0
while i < 20:
	print('\t',i)
	i+=1
	#break
	#continue
	#pass
else:
	print('Counting is finished')


print('-------------------------------------')
#find dublicates without using set
orgList =['a','b','c','b','d','m','n','n']
dubList = []

for ch in orgList:
	if orgList.count(ch)>1 and ch not in dubList:
		dubList.append(ch)

print (dubList)