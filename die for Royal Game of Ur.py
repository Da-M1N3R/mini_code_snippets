import random

diceUr = [0, 1, 2, 3, 4]

num = random.choices(diceUr, weights=[1, 4, 6, 4, 1], k=1)
print(num)
