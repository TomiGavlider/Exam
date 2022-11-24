import random

class Animal():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.fedTimes = 0

    def eat(self):
        self.fedTimes += 1

    def isHungry(self):
        self.checks = 0
        if self.name == 'Lion':
            return 'Hungry'
        elif self.name == 'Monkey':
            hungry = ['Not hungry','Hungry']
            return random.choice(hungry)
        elif self.name == "Elephant":
            self.checks += 1
            if self.checks > 1:
                return "Hungry"



    def toString(self):
        print(f'{self.name} is a {self.age} years old {self.gender} animal and was fed {self.fedTimes} times')


class Worker(Animal):
    def __init__(self,name,animalsToLookAfter):
        self.name = name
        self.animalsToLookAfter = animalsToLookAfter
    def dayli_routine(self):
        for animal in self.animalsToLookAfter:
            if animal is Animal.isHungry(self) == 'Hungry':
                self.fedTimes += 1







