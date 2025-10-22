def fun1(): 
    msg = "MNK"
    def fun2(): 
        print(msg) 
    fun2()
fun1()



def fun1(): 
    a = 45
    def fun2(): 
        nonlocal a 
        a=54
        print(a)
    fun2()
    print(a)
fun1()


def fun1(a):  
    def fun2():
        print(a)  
    return fun2 

closure_func = fun1("Hello, Closure!")
closure_func()



import logging
logging.basicConfig(level=logging.INFO) 

def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}") 
        return func(*args, **kwargs) 
    return wrapper

@logger
def add(a, b):
    return a + b  
print(add(3, 4))