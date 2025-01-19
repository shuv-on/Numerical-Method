import math

def f(x):
    """
    The function to find the root of.
    """
    return math.exp(-x) - x

def false_position(a, b, tol=1e-6, max_iter=100):
    """
    Implements the False Position method.

    Args:
        a: Lower bound of the initial interval.
        b: Upper bound of the initial interval.
        tol: Tolerance for convergence.
        max_iter: Maximum number of iterations.

    Returns:
        The root of the function.
    """
    if f(a) * f(b) >= 0:
        print("The interval [a, b] does not bracket a root.")
        return None

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c

if __name__ == "__main__":
    root = false_position(0, 1)  # Initial interval
    print(f"The root of the equation is: {root:.6f}")
