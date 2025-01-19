import math

def f(x):
    """
    The function to find the root of.
    """
    return math.exp(-x) - x

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    """
    Implements the Secant method.

    Args:
        x0: Initial guess for the root.
        x1: Second initial guess for the root.
        tol: Tolerance for convergence.
        max_iter: Maximum number of iterations.

    Returns:
        The root of the function.
    """
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(f(x2)) < tol:
            break
        x0 = x1
        x1 = x2

    return x2

if __name__ == "__main__":
    root = secant_method(0, 1)  # Initial guesses
    print(f"The root of the equation is: {root:.6f}")
