def zero(list):
    num = [0 for i in range(list.count(0))]
    zero = [i for i in list if i != 0]
    zero.extend(num)
    return(zero)

from random import randint

list = []

for i in range(10):
  list.append(randint(0,10))

print(zero(list))
