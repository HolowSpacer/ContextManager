from datetime import datetime
import time
import contextlib
from random import randint

@contextlib.contextmanager
def time_counter():
    try:
        start_time = datetime.now()
        yield
    finally:
        print('Время начала работы программы: ', start_time)
        print('Время окончания работы программы: ', datetime.now())
        print('Время работы программы: ', datetime.now() - start_time)

def generation_and_sort():
    empty_list = []
    for i in range(100000):
        empty_list.append(randint(1, 100000))
    return sorted(empty_list)

with time_counter():
    sorted_list = generation_and_sort()