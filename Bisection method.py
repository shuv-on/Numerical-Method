def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds a root of the function f using the bisection method.

    Args:
        f: The function to find the root of.
        a: The left endpoint of the interval.
        b: The right endpoint of the interval.
        tol: The desired tolerance for the root.
        max_iter: The maximum number of iterations to perform.

    Returns:
        The estimated root of the function.
    """

    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise ValueError("Bisection method did not converge within the maximum number of iterations.")

# Define the function
def f(x):
    return x**2 - 25

# Find the root using the bisection method
root = bisection_method(f, 0, 10)

print("The root of the equation is:", root)
