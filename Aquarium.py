
class fish:
    def __init__(self,name,weight,color):
        self.name = name
        self.weight = weight
        self.color = color


    def feed(self,type):
        if type == 'Kong':
            self.weight += 2
        elif type == 'Tang':
            self.weight += 1
            self.memory_loss = bool(random.choice([True, False]))
        elif type == 'Clownfish' and len(self.color) > 1:
            self.weight += 1

    def status(self):
        print(f"Name: {self.name}, Weight: {self.weight}, Color: {self.color}")


class aquarium(fish):

    fishes = []

    def add_fish(self,new_fish):

        self.fishes.append(new_fish)

    def feed(self,type):
        if type == 'Kong':
            self.weight += 2
        elif type == 'Tang':
            self.weight += 1
        elif type == 'Clownfish':
            self.weight += 1

    def remove_fish(self):
        for fish in self.fishes:
            if self.weigt >= 11:
                self.fishes.remove(fish)



    def get_status(self):
        print(f"Name: {self.name}, Weight: {self.weight}, Color: {self.color}")







