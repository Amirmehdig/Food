class Cart:
    def __init__(self):
        self.items = []

    def add(self, item: dict[int, int, float]):
        self.items.append(item)

    def remove(self, item: dict[int, int, float]):
        self.items.remove(item)

    def total(self):
        return sum([item.price for item in self.items])