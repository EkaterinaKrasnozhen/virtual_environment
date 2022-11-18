class Cars:
    v_engine = 1.5
    def __init__(self, color, brand): #внутри класса это метод
        self.color = color
        self.brand = brand
    def start(self):
        print(f'машина {self.color} {self.brand} поехала')
        
    def __str__(self):
        return f'{self.color} {self.brand}' #при print(my_car) вернет значения
        
my_car = Cars('red', 'lada')
print(my_car)
print(type(my_car))
your_car = Cars('black', 'bmv')
Cars.start(your_car)
