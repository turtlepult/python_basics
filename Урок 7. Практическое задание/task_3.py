class Worker():
    def __init__(self, *args):
        self.name = args[0]
        self.surname = args[1]
        self.position = args[2]
        self._income = {"wage": args[3], "bonus": args[4]}

class Position(Worker):

        def get_full_name(self):
            return self.name + ' ' + self.surname

        def get_full_income(self):
            return self._income['wage'] + self._income['bonus']

v_pet = Position("Ivan","Ladygin", "Merhc", 1000, 150)
print(f'Общий доход {v_pet.get_full_name()} составляет {v_pet.get_full_income()}')