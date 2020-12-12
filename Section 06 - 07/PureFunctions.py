#map, filter, zip, reduce ==> important pure function 

#MAP Function
def multiply_by_2(li):
    new_list=[]
    for i in li:
        new_list.append(i*2)
    return new_list

def multiply_by_3(item):
    return item*3
mylist = [1,2,3,4,5]
print("Multiply with 3: ",list(map(multiply_by_3,mylist)))
print("Original List  : ",mylist)

#FILTER Function
def only_odd(item):
    return item % 2 !=0

print("Filter only odds: ",list(filter(only_odd,mylist)))
print("Original List  : ",mylist)
