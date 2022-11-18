class Cars:
    v_engine = 1.5
    def __init__(self, color, brand): #внутри класса это метод
        self.color = color
        self.brand = brand
        self._code = 123454 # инкапсуляция, код не виден при выборе методов
    def start(self):
        print(f'машина {self.color} {self.brand} поехала')
        
    def __str__(self):#магический метод
        return f'{self.color} {self.brand}' #при print(my_car) вернет значения
    
    def _func(self): # с однм _ спереди - приватный метод, инкапсуляция - когда нужно скрыть и не показывать, два __ тоже не видно
        return
    
class SportCar(Cars): #наследование
    height_speed = 300
    
    
my_car = Cars('red', 'lada')
print(my_car)
print(type(my_car))
your_car = Cars('black', 'bmv')
Cars.start(your_car)


class Figure:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b
    
first = Figure(4,5)
s = first.area()
print(s)