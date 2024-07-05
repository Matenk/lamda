"""Задача №2 lamda """
list_ = [1, 2, 3, 4]
multi = map(lambda x: x ** 2, list_)
print(list(multi))

def multi(x):
    return x ** 2
result = map(multi, list_)

print(list(result))

"""Задача №1"""
def operate(n):

    if n != 0:
        def oper(x):
            return x / n
    else:
        def oper(x):
            return x * n
    return oper

list2_ = [2, 4, 6, 8]

by_1 = operate(2)
by_2 = operate(0)

result1 = map(by_1, list2_)
print(list(result1))
result2 = map(by_2, list2_)
print(list(result2))


"""Задача №3"""
class Repeater:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return f'Стороны прямоугольника равны: {self.value} и {n}, площадь равна: {self.value * n}'

repeat_five = Repeater(2)
print(repeat_five(3))