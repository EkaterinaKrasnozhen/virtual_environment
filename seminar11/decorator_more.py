def decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper')
        return func(*args, **kwargs)
    return wrapper


def my_func2(x,y):
    print('my func')
    return x * y


my_f = decorator(my_func2)
print(my_f(2,5))

def my_func4(x, y):
    print('my func 4')
    return x * y


# декоратор с параметрами
def constructor(param):
    def decorator2(func):
        def wrapper2(*args, **kwargs):
            print('wrapper 2')
            print(f'параметр декоратора {param}')
            return func(*args, **kwargs)
        return wrapper2
    return decorator2


c = constructor(0)
mf4 = c(my_func4)
print(mf4(3,4))

#google colab аналог jupyternotebook