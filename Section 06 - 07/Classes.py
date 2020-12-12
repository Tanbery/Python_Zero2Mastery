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

    @classmethod
    def adding_things(cls,num1, num2):
        return cls("Deneme",num1 + num2)
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2
#help(PlayerCharacter)

player1= PlayerCharacter("Enver", 20)
player1.run()
print(PlayerCharacter.adding_things2(1,2))
print(player1.adding_things(4,5))