# What is the output of the following code?

# from functools import reduce
# result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
# print(result)

"""
Answer
output is 24
reduce() is used  to apply a function 
to an iterable and reduce it to a single cumulative value.
"""

from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(result)

