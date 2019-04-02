# Ticket and Turtle game

import random as r


class Ticket:
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self, num):
        return self.exp * self.inc * self.discount * num

legal_x = [0, 10]
legal_y = [0, 10]


class Turtle:
    def __init__(self):
        self.energy = 100
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])

        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x

        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y < legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        self.energy -= 1

        return self.x, self.y

    def eat(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100


class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])

        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x

        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y < legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y

        return self.x, self.y

if __name__ == "__main__":
    # adult = Ticket()
    # child = Ticket(child=True)
    # print(adult.calcPrice(2) + child.calcPrice(1))

    turtle = Turtle()
    fish = []
    for i in range(10):
        new_fish = Fish()
        fish.append(new_fish)

    while True:
        if not len(fish):
            print("All The Fish Die, Game Over!!!")
            break
        if not turtle.energy:
            print("Turtle Has Out Of Energy, It Die!!!")
            break

        pos = turtle.move()

        for each_fish in fish:
            if each_fish.move() == pos:
                turtle.eat()
                fish.remove(each_fish)
                print("A fish has been eat")
