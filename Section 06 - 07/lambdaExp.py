#lambda expression
from functools import reduce 

mylist = [1 ,2 ,3 ]
yrlist = [10,20,30]
#MAP Function
def multiply_by_3(item):
    return item*3

print("Multiply with 3: ",list(map(multiply_by_3,mylist)))
print("Original List  : ",mylist)

print("Lambda multiply with 4: ",list(map(lambda item: item*4,mylist)))
print("Original List  : ",mylist)
#FILTER Function
def only_odd(item):
    return item % 2 !=0

print("Filter only odds: ",list(filter(only_odd,mylist)))
print("Original List  : ",mylist)

#ZIP Function ==> it creates new tuples
print("Zip two list  : ",list(zip(mylist,yrlist)))
print("Original Lists: ",mylist, yrlist)

#REDUCE Function
def accumulator(acc, item):
    #print(acc,item)
    return acc + item

print("Reduce the List: ",reduce(accumulator,mylist,0))
print("Original Lists: ",mylist)