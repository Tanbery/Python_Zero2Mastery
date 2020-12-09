#Conditional Logic 
is_old = True
is_licenced = False

if is_old:
    if is_licenced:
        print('You are old enough to drive and you have a licence')
    else:
        print('You are old enough to drive and you must apply for a licence')
else:
    print('You are too young to drive a car')
print('-------------------------------------')

#Ternary Operator
is_friend = False
can_msg = 'Message is allowed' if is_friend else 'Message is NOT allowed' #
print(can_msg)

Logical Operators
 < > == >= <= != and or not