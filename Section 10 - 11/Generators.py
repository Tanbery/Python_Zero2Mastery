#range(100) is a generator

#def make_list(num):
#    result = []
#    for i in range(num):
#        result.append(i*2)
#    return result
#my_list = make_list(100)
#print("my_list:", my_list)

#instead of creating whole list at once, it creates each item one by one.
def generator_func(num):
    for i in range(num):
        yield i

#for item in generator_func(1000):
#    print(item)

g = generator_func(10)
print("get Generator:",g)

while True:
    try:
        print(g)
        print(next(g))
    except :
        break

#Generator under hood
class MyGen():
    current=0
    def __init__(self, start, last):
        self.start=start
        self.last = last
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current +=1
            return num
        else:
            raise StopIteration

gen = MyGen(5,10)
for i in gen:
    print(i)

#---------------------------------------------------------------------------
#fibonacci with Generator
def fib(number):
    a = 0
    b = 1
    
    for i in range(number):
        yield a
        tmp = a
        a = b
        b = tmp + b

for item in fib(20):
    print(item)

