# Elliptic Curve: y^2 = x^3 + ax + b (mod p)

p = 17   # prime number
a = 2
b = 2

# Define point addition
def point_add(P, Q):
    if P == Q:
        return point_double(P)

    x1, y1 = P
    x2, y2 = Q

    m = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p

    return (x3, y3)


# Point doubling
def point_double(P):
    x, y = P

    m = ((3*x*x + a) * pow(2*y, -1, p)) % p
    x3 = (m*m - 2*x) % p
    y3 = (m*(x - x3) - y) % p

    return (x3, y3)


# Scalar multiplication (kP)
def scalar_mult(k, P):
    result = P
    for i in range(k - 1):
        result = point_add(result, P)
    return result


# Base point
G = (5, 1)

# Private key
d = 3

# Public key
Q = scalar_mult(d, G)

print("Private Key:", d)
print("Public Key:", Q)


# Encryption (simplified EC-ElGamal)
message = 7

k = 2  # random number

C1 = scalar_mult(k, G)
C2 = message + scalar_mult(k, Q)[0]

print("\nEncrypted:")
print("C1:", C1)
print("C2:", C2)


# Decryption
decrypted = C2 - scalar_mult(d, C1)[0]

print("\nDecrypted Message:", decrypted)