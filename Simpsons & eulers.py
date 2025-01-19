# Simpson's 1/3 Rule for Integration
def simpsons_13_rule(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n, 2):
        result += 2 * f(a + i * h)
    return (h / 3) * result

# Euler's Rule for Differentiation
def eulers_method(f, x0, h, steps):
    for i in range(steps):
        x0 = x0 + h * f(x0)
    return x0

# Function to be integrated
def func(x):
    return x ** 2

# Example usage
a = 0
b = 2
n = 2  # Number of intervals (even)
integral = simpsons_13_rule(func, a, b, n)
print(f"Approximate integral: {integral}")

# Function to differentiate
def func_derivative(x):
    return 2 * x

# Example usage for Euler's method
x0 = 1
h = 0.1
steps = 10
derivative = eulers_method(func_derivative, x0, h, steps)
print(f"Approximate derivative: {derivative}")
