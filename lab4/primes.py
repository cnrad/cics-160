def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def are_relatively_prime(num1, num2):
    minimum = num1 if num1 < num2 else num2

    for i in range(2, minimum + 1):
        if num1 % i == 0 and num2 % i == 0:
            return False
    return True

def primes(num):
    results = []

    for i in range(2, num + 1):
        if is_prime(i):
            results.append(i)

    return results

def prime_decomposition(num):
    results = []
    current_num = num
    i = 2

    while i * i <= current_num:
        if current_num % i != 0:   
            i += 1
        else:
            results.append(i)
            current_num //= i

    if current_num > 1:
        results.append(current_num)

    return results

# main program
if __name__ == '__main__':
    # candidate = int(input("Enter an integer: "))
    # if is_prime(candidate):
    # print (candidate, "is prime.")
    # else:
    # print (candidate, "is not prime")
    # print("is 2 prime?", is_prime(2))
    # print("are 2 and 7 relatively prime?", are_relatively_prime(2,7))
    # print("are 2 and 8 relatively prime?", are_relatively_prime(2,8))
    # print("are 4 and 8 relatively prime?", are_relatively_prime(4,8))
    # print("are 10 and 9 relatively prime?", are_relatively_prime(10,9))
    # print("prime numbers up to 7:", primes(7))
    # print("prime numbers up to 10:", primes(10))
    # print("prime numbers up to 2:", primes(2))
    print("prime numbers up to -3:", primes(-3))
