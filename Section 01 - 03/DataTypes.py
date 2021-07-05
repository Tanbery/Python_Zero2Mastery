#Binary Decimal and Typecast
print(bin(5))
print(int('0b101', 2))
print(type(5))
print('---------------------------')
#Variables
a, b, c = 1, 2, 3
print('a : ' + str(a))
print('b : ' + str(b))
print('c : ' + str(c))
print('---------------------------')
#string
print('Helloo' + ' Enver')

name = 'Enver'
age = 39
print(f'Hello {name}. You are {age} years old')
print('Hello {0}. You are {1} years old'.format(name, age))
print('---------------------------')

#[start:stop:stepover]
selfish = "0123456789"

print('selfish        --> ' + selfish)
print('length(selfish)--> ' + str(len(selfish)))
print('selfish[0]     --> ' + selfish[0])
print('selfish[0:2]   --> ' + selfish[0:2])
print('selfish[0:8:2] --> ' + selfish[0:8:2])
print('selfish[1:]    --> ' + selfish[1:])
print('selfish[:5]    --> ' + selfish[:5])
print('selfish[::1]   --> ' + selfish[::1])
print('selfish[-1]    --> ' + selfish[-1])
print('selfish[::-1]  --> ' + selfish[::-1])
print('---------------------------')
#[start:stop:stepover]
is_cool = False
print('is cool? ' + str(is_cool))

#print('---------------------------')
#birthYear= input('What year were you born?')
#age = 2020 - int(birthYear)
#print(f'You were born at {birthYear} and you are {age} years old')


print('---------------------------')
amz_cart = [
   'notebooks'
  ,'sunglasses'
  ,'toys'
  ,'grapes'
]
new_cart = amz_cart[:] #copy whole list as a new list
amz_cart[0] = 'laptop'
print('new cart:')
print(new_cart)
print('amz cart:')
print(amz_cart)

#adding methods
amz_cart.append(  "deneme123") #no return 
amz_cart.insert(2,"deneme345") #no return 
amz_cart2 = amz_cart.extend("deneme567")

#removing
#amz_cart.pop() #remove lastone or indexed one and return the removed item
#amz_cart.remove('toys') #remove by value and no return
#amz_cart.clear() #remove all 

#Index
amz_cart.index('sunglasses') #return first index
amz_cart.count('sunglasses') #return numbers of item
amz_cart.sort() #sort the orjinal list
sorted(amz_cart) #sort the list and create a new list 
amz_cart.copy() #amz_cart[:]
amz_cart.reverse # amz_cart[::-1]

#Range and Join
basket  = list(range(1  ,100))
print('basket')
print(basket)

#list unpacking
a,b,c,*others,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(others)
print(d)


print('---------------------------')
#Dict --> hashmap
#Key needs to be hashable(immutable)
#dictionary is unordered. 
dictionary = {
   'a'  :[1,2,3]
  ,'b'  :'hello'
  ,'c'  :True
  ,True :4
  ,100  :5
  ,'x'  :99
}

print(dictionary['a']) #if no key, error will raise
print(dictionary.get('b','None')) #if no key , it uses the default value
print('a' in dictionary)
print('a' in dictionary.keys())
print('a' in dictionary.items())
#dictionary.clear()
#new_dict = dictionary.copy()
#dictionary.pop('a')
dictionary.update({'x':105})#if no key value, it creates new key+value pair
print(dictionary)

#print('---------------------------')
##Tuple...
##Tuple is immutable...
#my_tuple = (1,2,3,4,5,6,7,8,9,5,5,6)
#print(my_tuple[1:5])
#print(my_tuple.count(5))
#print(my_tuple.index(6))

#print('---------------------------')
##Sets
##unordered collection of UNIQUE object
#my_set = {1,2,3,4,5,6,7,8,9,5,6,}
#print(my_set)
#my_set.add(100)
#my_set.add(5)
#print(my_set)
#my_set.difference(your_set)
#my_set.difference_update(your_set)
#my_set.discard(5)
#my_set.intersection(your_set) # print(my_set & your_set)
#my_set.isdisjoint(your_set) #if both sets are tottaly different, returns True
#my_set.union(your_set) # print(my_set | your_set)
#my_set.issubset(your_set)
#my_set.issuperset(your_set)