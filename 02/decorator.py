import time
from collections import deque

def mean(n):
    def decorator(func):
          time_arr = deque(maxlen = n)
          def wrapper(*args, **kwargs):
                start = time.time()
                res_func = func(*args, **kwargs)
                end = time.time()
                time_arr.append(end - start)
                av_time = sum(time_arr) / len(time_arr)
                print(f'The last {n} calls. Average time: {av_time}')
                return res_func
          return wrapper
    return decorator
