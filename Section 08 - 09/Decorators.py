#decorators --> @classmethod, @staticmethod
#functions are like a variables. 

from time import time

def hello0():
    print("Helloooooo")
greet = hello0
greet()


def hello1(funct):
    funct()

def greet1 ():
    print("Still here")

hello1(greet1)

#Higher Order Function
def greet2(func): #Accept function as parameter like MAP, Filter, Reduce  function 
    funct()

def greet3():
    def func():
        return 5
    return funct #Return Function as returnvalue
#---------------------------------------------------------------------------------------------
def my_decorator(funct):
    def wrap_func(*args,**kwargs):
        print("*************")
        funct(*args,**kwargs)
        print("*************")
    return wrap_func

@my_decorator
def hello():
    print("Hellooooo")

@my_decorator
def bye():
    print("Bye bye")

hello() #my_decorator(hello)()
bye()   #my_decorator(bye)()
#----------------------------------------------------------------------------------------------

def myPerformanceDecorator(func):
    def wrap_func(*args, **kwargs):
        t1= time()
        result = func(*args,**kwargs)
        t2= time()
        print(f"took {t2-t1} ms")
        return result
    return wrap_func

@myPerformanceDecorator
def long_time():
    for i in range(0,10000):
        i*5
long_time()
