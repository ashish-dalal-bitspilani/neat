import time
from random import randint

def time_consumption(func):
    def wrap_time(*args, **kwargs):
        begin = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} execution duration : {end-begin} seconds")
        return output
    return wrap_time

@time_consumption
def generate_random_numbers(n: int)-> list[int]:
    random_numbers = []
    for i in range(n):
        random_numbers.append(randint(1,n))
    return random_numbers

generate_random_numbers(10000000)