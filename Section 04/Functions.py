#Functions
#basic functions
def say_hello():
	print("Hello world from functions")
say_hello() #call function

#argument vs parameters
def say_hello2(name ='Vader', emoji=':-))'):
	print(f'Hello {name} {emoji}')
#call functions with argument
say_hello2("Enver",":)") 
say_hello2("Simru",":)") 
say_hello2("Haibo",":(") 

#keyword argument 
say_hello2(emoji = ":-D", name = "Bibi") #dont use this
say_hello2( name = "Bibi", emoji = ":-D")
say_hello2() #call with default parameters
say_hello2('Timmy') #call with default parameters


def topla(num1,num2):
	return num1+num2 #return value from function
print(topla(10,5))

#methods vs functions
def test(a):
	'''
	Info: this function tests and prints param a
	'''
	print(a)

test("!!!!!!")


# *args and **kwargs
#Rule: params, *args, default params, **kwargs
def super_func(*args,**kwargs):
	print(args,kwargs)
	return sum(args) + sum(kwargs.values())

print(super_func(1,2,3,4,5,num1=10,num2=15))


def highest_even(li):
    nHighest = -1
    for i in li:
        if i % 2 == 0 and nHighest < i:
            nHighest = i
    return nHighest if nHighest != -1 else None

def highest_even2(li):
    evens = []
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)

##print(highest_even([1,3,5]))
print(highest_even([1, 3, 5]))

#Walrus operator
def uzunluk(msg):
	if (n:=len(msg)) > 10:
		print(f'Too long {n} elements')
uzunluk('Helloooooooooooooooo')