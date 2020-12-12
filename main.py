class User:
    def  sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name ,power):
        self.name= name 
        self.power = power
    def attack(self):
        print(f"attack with power {self.power}")

class Archer(User):
    def __init__(self, name ,num_arrow):
        self.name= name 
        self.num_arrows = num_arrow
    def attack(self):
        print(f"attack with power {self.num_arrows}")

wz1= Wizard("Merlin",50)
ar1= Archer("Robin",100)
print(wz1.sign_in())

wz1.attack()
ar1.attack()