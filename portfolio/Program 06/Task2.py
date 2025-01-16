#Write and test a function that takes an integer as its parameter and returns the factors of that integer.
#(A factor is an integer which can be multiplied by another to yield the original).

def find_factors(n):
    if n == 0:
        raise ValueError("Zero does not have factors.")
    n = abs(n)
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i: 
                factors.append(n // i)
    return sorted(factors)

num = int(input("Enter a number: "))
print(f"Factors of {num}: {find_factors(num)}")