import datetime
from functools import wraps
import time

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper


def decorator(func):
    @wraps(func) #скрыть работу декоратора и через __doc__ будет видна сама функция
    def wrapper(*args, **kwargs):
        #a, b = args
        #res  = 2 * (a + b)
        log_msg = f'{datetime.datetime.now():%d.%m.%y %H:%M:%S}\t'
        log_msg += f'{func.__name__}\t'
        # табуляция пробел
        log_msg += f"параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        #print(f'площадь комнаты = {res}')
        log_msg += f'результат: {res}\n'
        print(log_msg)
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res
    return wrapper


def logg_func(log_lvl=0):#декоратор с параметром
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_msg = f'{datetime.datetime.now():%d.%m.%y %H:%M:%S}\t'
            if log_lvl == 1:
                log_msg += f'{func.__name__}\t'
                log_msg += f"параметры: {', '.join(map(str, args))}\t"
            res = func(*args, **kwargs)
            log_msg += f'результат: {res}\n'
            print(log_msg)
            with open('log_file.log', 'a', encoding='utf-8') as fp:
                fp.write(log_msg)
            return res
        return wrapper
    return decorator


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish-start)
        return res
    return wrapper


def cacher(func):
    cach = {}
    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[args] = func(*args)
        print(cach)
        return cach[args]
    return wrapper
        


#@logg_func(0)  # убрать декоратор чтобы распечатать .__doc__
@cacher
def room_area(x, y):
    """Функция возвращает

    Args:
        x - длина
        y -ширина

    Returns:
        площадь
    """
    return x*y


#room_area(4, 5)

# def main():
# print(room_area(5,4))
# print(room_area.__doc__)
# help(room_area(3, 4)) #справка по функции


@timer
def main():
    print(room_area(3, 4))
    print(room_area(3, 4))
    print(room_area(2, 8))
    print(room_area(2, 8))
    print(room_area(2, 7))


main()

# if __name__ == '__main__':
# main()


# main()
