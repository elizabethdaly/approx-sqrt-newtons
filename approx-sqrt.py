# Adapted from Go: 

def sqrt(x):
    # Initial guess
    z  = 1.0
    # Keep getting a better esitimate for sqrt(x) until you are within
    # two decimal places.
    while abs(z * z - x) >= 0.01:
        # get a better approx for sqrt.
        z -= (z * z - x) / (2 * z)
return z

sqrt(8.0)