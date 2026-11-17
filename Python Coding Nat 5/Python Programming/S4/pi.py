from decimal import Decimal, getcontext

def calculate_pi(digits):
    """Calculates pi to a specified number of digits using the Chudnovsky algorithm."""
    if digits < 1:
        return "3"

    getcontext().prec = digits + 3
    
    # Chudnovsky algorithm constants
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    iterations = (digits // 14) + 1
    
    for i in range(1, iterations):
        M = (M * (K**3 - 16*K)) // i**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
        
    pi = C / S
    

    return str(pi)[:digits + 2]

digits_needed = 10000
pi_string = calculate_pi(digits_needed)

print(f"Pi to {digits_needed} digits:")
print(pi_string)
