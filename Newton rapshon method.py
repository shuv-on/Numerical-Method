import math

def f(x):
    """
    The function to find the root of.
    """
    return math.exp(-x) - x

def df(x):
    """
    The derivative of the function.
    """
    return -math.exp(-x) - 1

def newton_raphson(x0, tol=1e-6, max_iter=100):
    """
    Implements the Newton-Raphson method.

    Args:
        x0: Initial guess for the root.
        tol: Tolerance for convergence.
        max_iter: Maximum number of iterations.

    Returns:
        The root of the function.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-8:
            print("Derivative is zero, stopping.")
            break
        x = x - fx / dfx
        if abs(fx) < tol:
            break
    return x

if __name__ == "__main__":
    root = newton_raphson(0.5)  # Initial guess
    print(f"The root of the equation is: {root:.6f}")
