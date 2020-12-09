#scope ===> what variable do i have access to?
#1 - start with local
#2 - parent local?
#3 - Global
#4 - Built in python function

a = 1
def conf1():
	a = 2
	return a
def conf2():
	global a #global or nonlocal can be used
	a= 3
	return a

def conf3(a):
	a= 4
	return a

print("once  ", a)
print("exec  ", conf1())
print("sonra ", a)

print("once  ", a)
print("exec  ", conf2())
print("sonra ", a)

print("once  ", a)
print("exec  ", conf3(a))
print("sonra ", a)

print|("Hello Naber?")