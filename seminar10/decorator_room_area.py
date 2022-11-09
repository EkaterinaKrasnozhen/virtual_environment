import datetime
from functools import wraps

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #a, b = args
        #res  = 2 * (a + b)
        log_msg = f'{datetime.datetime.now():%d.%m.%y %H:%M:%S}\t'
        log_msg += f'{func.__name__}\t'
        log_msg += f"параметры: {', '.join(map(str, args))}\t" #табуляция пробел
        res = func(*args, **kwargs)
        #print(f'площадь комнаты = {res}')
        log_msg += f'результат: {res}\n'
        print(log_msg)
        with open ('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res
    return wrapper

@decorator #убрать декоратор чтобы распечатать .__doc__
def room_area(x, y):
    """Функция возвращает

    Args:
        x - длина
        y -ширина

    Returns:
        площадь
    """
    return x*y

room_area(4,5)

#def main():
    # print(room_area(5,4))
    # print(room_area.__doc__)
    #help(room_area(3, 4)) #справка по функции 

# if __name__ == '__main__':
#     main()