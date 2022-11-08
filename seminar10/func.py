# def my_func(x, y, *args):
#     print(f'{x = }')
#     print(f'{y = }')
#     other = args
#     print(other)
    
# my_func(2,3,15,4,13)


# def my_func2(x, y, *, a, b, c): #* или / отделяем позиционные параметры x,y от именованных a,c,b
#     print(f'{x = }')
#     print(f'{y = }')
#     print(f'{a = }')
#     print(f'{b = }')
#     print(f'{c = }')
    
# my_func2(1, 3, c=2, b=4, a = 7)


# def my_func3(*args, **kwargs):
#     a = args
#     b = kwargs
#     print(f'{a = }')
#     print(f'{b = }')
    
# my_func3(1, 2, 3, 4, 5, z=12, x=15, y=1) #получим позиционные параметры args и словарь kwargs x : 15 ключ: значение


def my_func4(*args, **kwargs):
    a, b, *c = args
    d = kwargs
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')
    print(f'{d = }')
    
my_func4(1, 2, 3, 4, 5, z=12, x=15, y=1) # распаковали a=1,b=2, c= остальные позиционные