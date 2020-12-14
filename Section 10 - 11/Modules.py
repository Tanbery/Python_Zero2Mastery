#import Utility 
from Utility import multiply,divide
import random
import sys
#if Mudule is under a folder, you can use package. 
#if your module is under a folder, there must be __init__.py file. 
#import shopping.shopping_cart
#import shopping.more_shopping.shopping_cart
#from shopping.more_shopping.shopping_cart import buy ===> you can call Buy function without pkg information
#from shopping.more_shopping import shopping_cart 

#print(Utility)
#print(Utility.multiply(1,2))
#print(Utility.divide(6,2))
print(multiply(1,2))
print(divide(6,2))
#__name__ = __main__ is given the first run file
# __name__ = file name or package name is given for other files
print("Module Name: ",__name__)
myList = [1,2,3,4,5]
help(random)
print("Dir Random:", dir(random))
print("Random Function:",random.random())
print("randint Function:",random.randint(1,20))
print("Choice Function:",random.choice(myList))
print("Before shuffle Function:",myList)
random.shuffle(myList)
print("After  shuffle Function:",myList)

print(sys.argv)# argv[0]=> filename, argv[1]==>first parameter