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
