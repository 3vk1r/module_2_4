numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_primes = []
for i in range(len(numbers)):
    is_prime = True
    for j in range(2, numbers[i]):
        if numbers[i] != 1 and numbers[i] % j == 0:
            is_prime = False
            break
    if numbers[i] == 1:
        continue
    if is_prime == True:
        Primes.append(numbers[i])
    else:
        Not_primes.append(numbers[i])
print(Primes, '\n', Not_primes)