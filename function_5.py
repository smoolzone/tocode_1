from typing import Any, Tuple, Union

import numpy as np
from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)
# assert isinstance(num2, int)
x = int(np.lcm(num1, num2))

print(num1)
print(num2)
print(int(x))

num1 = int(input("Type your first no.: "))
num2 = int(input("Type your second no.: "))

x = np.lcm(num1, num2)
print(x)
