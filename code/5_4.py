from datetime import datetime


def decorator(func):
    def wrapper(x):
        starting_time = datetime.now()
        func(x)
        print(f"Время выполнения функции: {(datetime.now() - starting_time)}")
    return wrapper

@decorator
def count_elements(my_list_1):
    x = 0
    for item in my_list_1:
        x += 1
    print(f"В списке {x} элементов")

@decorator
def filter_list(my_list_2):
    print(list(filter(lambda x: x >= 0, my_list_2)))


count_elements([1, 2, 3, 4, 5])
filter_list([-2, -1, 0, 1, 2, 3, 4])