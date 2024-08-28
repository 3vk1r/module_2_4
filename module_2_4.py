numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_primes = []
for number in numbers:
    is_prime = True
    for j in range(2, number):
        if number != 1 and number % j == 0:
            is_prime = False
            break
    if number == 1:
        continue
    if is_prime == True:
        Primes.append(number)
    else:
        Not_primes.append(number)
print(Primes, '\n', Not_primes)