class Worker:
    def __init__(self, name, surname, position, wege, bonus):
        self.name =name
        self.surname = surname
        self.position = position
        self._income = {'profit': wege, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self._income.values())}'

meneger = Position('Dorian', 'Grey', 'CEO', 500000, 125000)
print(meneger.get_full_name)
print(meneger.position)
print(meneger.get_full_profit())