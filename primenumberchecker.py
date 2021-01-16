import math
def isPrime(num, with_factors=False):
    if num < 2:
        # Returns False if number is 0, 1 or negative as these aren't prime
        return [] if with_factors else False
    if num in [2, 3]:
        return [num] if with_factors else True
    # Making a list of all factors
    factors = [i for i in range(2, int(math.sqrt(num)) + 1) if num%i == 0]
    # Checking and returning whether the factors list is empty or not.
    return factors if with_factors else (not bool(factors))

if __name__ == "__main__":
    number = int(input("Enter number: "))
    # Demonstrating UseCase1
    print(number, "is", ("" if isPrime(number) else "not"), "a prime number")
    # Demonstrating UseCase2
    for fact in isPrime(number, with_factors=True):
        print(f"{fact}*{number//fact}={number}")
