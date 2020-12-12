#OOP
#no private things in python. use _name as convention.
class PlayerCharacter:
    membership = True #class Object attribute

    def __init__(self,name,age):
        self.name= name
        self.age = age

    def run(self):
        print("Run ",self.name)

    def shout(self):
        print(f"My name is {self.name}")

    #class itself will be default parameter in this function. 
    #we must call this funtion with Obj.method()
    @classmethod
    def adding_things(cls,num1, num2):
        return cls("Deneme",num1 + num2)
    
    #this method can be called without object. 
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2
#help(PlayerCharacter)

player1= PlayerCharacter("Enver", 20)
player1.run()
print(PlayerCharacter.adding_things2(1,2))
print(PlayerCharacter.adding_things(4,5))
print(player1.adding_things(4,5))



#super class
class User:
    def __init__(self, email):
        self.email = email

    def  sign_in(self):
        print("logged in")

    def attack(self):
        print("Base Attack Function: do nothing")


#subclasses
class Wizard(User):
    def __init__(self, name ,power,email):
        #User.__init__(self,email)
        super().__init__(email)
        self.name= name 
        self.power = power
        

    def attack(self):
        print(f"attack with power {self.power}")

class Archer(User):
    def __init__(self, name ,num_arrow):
        self.name= name 
        self.num_arrows = num_arrow

    def attack(self):
        User.attack(self) #we can call base function from subclasses
        print(f"attack with power {self.num_arrows}")

wz1= Wizard("Merlin",50,"Merlin@enver.com")
ar1= Archer("Robin",100)
print(wz1.sign_in())

wz1.attack()
ar1.attack()

print("Wizard is User? ",isinstance(wz1,User))
print("Archer is User? ",isinstance(ar1,User))
print("Wizard is Object? ",isinstance(wz1,object))
print("Archer is Object ",isinstance(ar1,object))

print("\nPolymophozm Attack Call")
for usr in [wz1, ar1]:
    usr.attack()

#how to call super()
print("\nSuper class contructor call")
print("Wizard email: ", wz1.email)

#Dunder Methods
print("\nDunder Methods")
print("Dunder Methods: ", dir(wz1))

#check the method resolution order
#print(wz1.__mro__)

class Toy():
    def __init__(self, color, age):
        self.color  = color
        self.age    = age
    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5
    
    #def __del__(self):
    #    print("Deleted")

    def __call__(self):
        return "Yes??"

    def __getitem__(self,i):
        return self.color if i == 0 else self.age

act = Toy('Red', 20)
print('__str__() Method: ',act.__str__())
print('str() Type cast: ',str(act))
print('len() Method: ', len(act))
#del(act)
print('__call__() Method: ', act())
print('__getitem__() Method: ', act[0], act[1])

class SuperList(list):
    def __len__(self):
        return 100


slist = SuperList()
print(len(slist))
slist.append(5)
print(slist[0])

print(issubclass(SuperList,list))
print(issubclass(list,object))