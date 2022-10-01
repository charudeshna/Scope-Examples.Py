a = 20
b = 10

def func():
    return a + 1

def func():
    b = 20
    return a + b

def func():
    a = 20
    b = 20
    return a + b

def func():
    result = a + b
    a = 20
    b = 20

def func():
    a = a + 1
    b = b + 1
    return a + b

def func():
    a=20
    def wrapper():
        a=30
        return a+1
    return wrapper()


def func():
    a = 10
    def wrapper():
        a = 300
        a = a + 1
    return wrapper()

