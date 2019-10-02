# Adapted from Go: 

def sqrt(x):
    # Initial guess
    z  = 1.0
    # Keep getting a better esitimate for sqrt(x) until you are within
    # two decimal places.
    while abs(z * z - x) >= 0.00001:
        # get a better approx for sqrt.
        z -= (z * z - x) / (2 * z)
    return z

# Calculate the square root of 8.
z = sqrt(63.0)
# Print z
print(z)
# Print z^2.
print(z * z)