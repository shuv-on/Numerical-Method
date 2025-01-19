import numpy as np

def determinant(matrix):
    """
    Calculates the determinant of a matrix.
    """
    return np.linalg.det(matrix)

def cramer_rule(coefficients, constants):
    """
    Solves a system of linear equations using Cramer's Rule.

    Args:
        coefficients: A list of lists representing the coefficients of the variables.
        constants: A list of constants.

    Returns:
        A list of solutions for the variables, or None if Cramer's Rule is not applicable.
    """
    coefficients = np.array(coefficients)  # Convert to NumPy array
    constants = np.array(constants)  # Convert to NumPy array
    n = len(coefficients)
    D = determinant(coefficients)

    if D == 0:
        return None  # Cramer's Rule is not applicable

    solutions = []
    for i in range(n):
        Dx = coefficients.copy()  # Create a copy of the coefficient matrix
        Dx[:, i] = constants  # Replace the i-th column with the constants
        Dx_det = determinant(Dx)  # Compute the determinant of the new matrix
        solutions.append(Dx_det / D)  # Compute the solution for the i-th variable

    return solutions

# Example Usage
coefficients = [[3, 2], [1, -1]]
constants = [1, 5]
solutions = cramer_rule(coefficients, constants)

if solutions:
    print("Solutions:", solutions)
else:
    print("Cramer's Rule is not applicable.")
