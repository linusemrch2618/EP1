import numpy as np

def test(a, b=3, c=False):
    x = np.array([i * b for i in range(a)])
    if c:
        x = x ** 2
    return x
    a = -100  # This line is unreachable due to the return statement above

# Simulating the code's behavior
result_1 = test(2, 2)
#result_2 = a
result_3 = test(1)
result_4 = test(3, c=True)[-1]
result_5 = test(5)[1:3]

# Output
print(result_1)
#print(result_2)
print(result_3)
print(result_4)
print(result_5)
