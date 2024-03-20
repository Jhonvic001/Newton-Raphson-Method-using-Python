def f(x):
    return 4*x**4 - 3*x**3 - 6*x**2 - 2*x - 1

def f_prime(x):
    return 16*x**3 - 9*x**2 - 12*x -2

def round_to_four_decimal_places(num):
    return round(num, 4)

def newton_raphson(initial_guess, tolerance=1e-6, max_iterations=100):
    x0 = initial_guess
    for i in range(max_iterations):
        fx0 = f(x0)
        if abs(fx0) < tolerance:
            print(f"Root found at x = {round_to_four_decimal_places(x0)} after {i+1} iterations.")
            return round_to_four_decimal_places(x0)
        f_prime_x0 = f_prime(x0)
        if f_prime_x0 == 0:
            print("Derivative is zero. Cannot continue.")
            return None
        x1 = x0 - fx0 / f_prime_x0
        print(f"Iteration {i+1}: x_{i+1} = {round_to_four_decimal_places(x1)} (Before division: {round_to_four_decimal_places(x0)} - ({round_to_four_decimal_places(fx0)} / {round_to_four_decimal_places(f_prime_x0)}))")
        if abs(x1 - x0) < tolerance:
            print(f"Root found at x = {round_to_four_decimal_places(x1)} after {i+1} iterations.")
            return round_to_four_decimal_places(x1)
        x0 = x1
    print("Root not found within maximum iterations.")
    return None

# Example usage:
initial_guess =4  ######### Initial guess for the root
newton_raphson(initial_guess)
