# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]

#1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)

from functools import wraps
import time
import datetime

def logger_timer(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        log_msg = f'start {time.time_ns()}\t'
        log_msg += f'finish {time.time_ns()}'
        log_msg += f'{func.__name__}\t'
        log_msg += f"параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        log_msg += f'результат: {res}\n'
        print(log_msg)
        with open('seq_n.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res
    return wrapper


def cacher(func):
    cach = {}
    @wraps(func)
    def wrapper(*args):
        key = args #ключ записывается с запятой почему-то
        if key not in cach:
            cach[args] = func(*args)
        print(cach)
        return cach[args]
    return wrapper


@logger_timer
@cacher
def seq(n):
    li = [x for x in range(0,n)]
    res = list(map(lambda x: (1+x) ** x, li))
    return res
    

def main():
    print(seq(5))
    print(seq(5))
    print(seq(6))
    print(seq(3))
    print(seq(3))


main()