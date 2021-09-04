class Bascara_1():
    def __init__(self):
        self.x = 0
        return print('Entrou na Bascara_1')

    def calc_bas(self, val):
        self.x = val
        return self.x

class Bascara_2():
    def __init__(self, val):
        self.x = val
        return print('Entrou na Bascara_2')

    def calc_bas(self):
        return self.x
