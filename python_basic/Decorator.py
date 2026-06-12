def deco(func):
    def inner(*args):
        print("Started..")
        func(*args)
        print("Ended...")
    return inner

@deco
def add(a, b):
    print("Addition :",a+b)
add(10, 3)

@deco
def sub(a, b, c):
    print("Subtraction :", a-b-c)
sub(10, 3, 2)

