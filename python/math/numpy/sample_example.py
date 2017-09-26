import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 2, 3])

print a + b
print a - b
print a / b

# Note this is element wise multiplication and not matrix multiplication
print a * b

# Matrix multiplication is done by dot function
print np.dot(a, b)

# Take a transpose using .T
print a.T

# Key feature of numpy is using Broadcasting
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])

# This is where all the magic happens
y = x + v

print y