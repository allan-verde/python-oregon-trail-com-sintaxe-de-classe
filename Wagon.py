class Wagon():
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.passengers = []

    def get_available_seat_count(self):
        return self.capacity - len(self.passengers)

    def join(self, traveler):
        if self.get_available_seat_count() > 0:
            self.passengers.append(traveler)
        else:
            print('carrocha cheia')
            return 'A carrocha já está cheia'

    def should_quarantine(self):
        for traveler in self.passengers:
            if traveler.is_healthy == False:
                return True
        return False

    def total_food(self):
       return sum([traveler.qtfood for traveler in self.passengers])