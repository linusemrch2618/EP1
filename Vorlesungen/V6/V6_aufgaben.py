import matplotlib.pyplot as plt
def number_of_divisors(n):
    return len([i for i in range(1, n+1) if n % i == 0])
def is_prime(n):
    return number_of_divisors(n) == 2
def number_with_most_divisors(n):
    return max(range(1, n+1), key=lambda _: number_of_divisors(_))

x=list(range(1, 1001))
y=[number_of_divisors(i) for i in x]
plt.plot(x,y,'ro')
plt.show()
plt.hist(y, bins=range(1,34), rwidth=0.8)
plt.show()