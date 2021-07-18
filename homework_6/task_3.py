def is_prime(number: int) -> bool:
    """
    Verifies is a number prime
    """

    d = 2
    while number % d != 0:
        d += 1
    return d == number


if __name__ == "__main__":
    print(is_prime(12))

# Perfect. Best solution for current homework I have ever see.
