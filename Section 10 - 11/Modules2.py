from collections import Counter, defaultdict,OrderedDict
import datetime
import time
from array import array

li1 = [1,2,3,4,5,6,7,7]
li2 = 'blah blah blah thinking about python'
print(Counter(li1))
print(Counter(li2))

#di = defaultdict(int,{'a':1,'b':2 }) # it will call int() for no  exist key
di = defaultdict(lambda:'Does\'t exist',{'a':1,'b':2 }) 
print(di['c'])
print('-------------------------------')
print(datetime.time())
print(datetime.time(5,45,2))
print('Today:',datetime.date.today())
print(time.time())

arr = array('i', [1,2,3,4,5,6])
print(arr)