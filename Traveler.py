class Traveler():
    def __init__(self, name) -> None:
        self.name = name
        self.qtfood = 1
        self.is_healthy = True

    def hunt(self):
        self.qtfood += 2

    def eat(self):
        if self.qtfood > 0:
            self.qtfood -= 1
        else:
            self.is_healthy = False
