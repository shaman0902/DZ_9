class Stationery:
    def __init__(self, title='Something that can draw'):
        self.title =title

    def draw(self):
        print(f'Just start drawing! {self.title}))')

class Pen(Stationery):
    def draw(self):
        print(f'Start drewing with {self.title} pen!')

class Pensil(Stationery):
    def draw(self):
        print(f'Start drewing with {self.title} pensil!')

class Marker(Stationery):
    def draw(self):
        print(f'Start drewing with {self.title} marker!')
