import random

class CAB:
    def game(self):
        self.listnum = [random.randint(0, 9) for n in range(4)]
        print("Secret number = " + str(self.listnum))

        self.count = 0
        while True:
            self.count += 1
            print("Guess: " + str(self.count))

            print("Please guess " + str(4) + "-digit number: ")
            self.guess = [int(i) for i in str(input())]

            if self.guess == self.listnum:
                print("You won.")
                break

            else:
                cow = 0
                bull = 0

                for x in range(0, 4):
                    if self.guess[x] == self.listnum[x]:
                        cow += 1
                    elif self.guess[x] in self.listnum:
                        bull += 1

            print("Cows: " + str(cow) + " Bulls: " + str(bull))
    def guess(self):
        print("It took you " + str(self.count) + " guess(es).")
    def state(self):
        if self.guess == self.listnum:
            return 'Finished'
        else:
            return 'Playing'
