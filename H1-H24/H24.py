import time

def logger(mesagge_type):
    def decorator(func):
        if mesagge_type == "wrapper":
            def wrapper(*args, **kwargs):
                now = time.time()
                print(f'Function {func.__name__} was called at {now}')
                return func(*args, **kwargs)
            return wrapper
        if mesagge_type == "warn":
            def warm_func(*args):
                print(f"\033[38;2;255;0;0mWARN:\033[0m args can't be strings")
                return func(*args)
            return warm_func
        if mesagge_type == "info":
            def info_func(*args):
                print(f"\033[38;2;255;255;0mInfo:\033[0m name - {func.__name__}, qualname  - {func.__qualname__}, module - {func.__module__}")    
                return func(*args)
            return info_func  
    return decorator

@logger("info")
@logger("warn")
@logger("wrapper")

def sume(a, b):
    return a + b

print(sume(5,19))
