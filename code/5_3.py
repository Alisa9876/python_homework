res = ('кот', 'дед', 'заказ', 'число', 'филин')

print(tuple(filter(lambda str: str == str[::-1], res)))