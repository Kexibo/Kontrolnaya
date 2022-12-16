"""
7. Класс Добрый Ифрит (GoodIfrit) Экземпляр класса инициализируется с 
аргуметами: высота, имя доброта. Класс должен реализовывать 
функциональность  -- change_goodness(value)
"""
class GoodIfrit:
    def __init__(self, visota, name, goodness):
        self.visota = visota
        self.name = name
        self.goodness = goodness

    def change_goodness(self, value):
        if value <= 0:
            self.goodness = 0
            print('Доброта равна 0')
        else:
            self.goodness = value
            print(f'Доброта равна {value}')

    def sloshenie(self, number):
        print(self.name + str(number))
        g = GoodIfrit(self.visota+number, self.name+str(number), self.goodness)

    def vozvr(self, arg):
        print(arg * self.goodness // self.visota)

    def __str__(self):    
        return 'Good Ifrit {}, {}'.format(self.visota, self.goodness) 

    #def vsvod(self):
     #   print(f'Good Ifrit {self.visota}, {self.goodness}')

    def __gt__(self, other):
        return self > other

    def __lt__(self, other):
        return self < other

    def srav(self, other):
        if self.visota > other.visota:
            print('Наш ифрит выше')
        elif self.visota < other.visota:
            print('Наш ифрит ниже')
        else:
            print('Они одинаковы')
        
        if self.name < other.name:
            print('Наш ифрит раньше в алфавите')
        elif self.name > other.name:
            print('позже в алфавите')
        else:
            print('Они равны')
        
        if self.goodness > other.goodness:
            print('Наш ифрит добрее')
        elif self.goodness < other.goodness:
            print('Наш ифрит менее добрый')
        else:
            print('Они равны')


ignat = GoodIfrit(15, 'Игнат', 50)
print(ignat.goodness)
ignat.change_goodness(30)
print(ignat.goodness)
ignat.sloshenie(1)
ignat.vozvr(10)
print(ignat.__str__())
vitalik = GoodIfrit(17, 'Виталик', 70)
ignat.srav(vitalik)
