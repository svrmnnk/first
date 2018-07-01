primes = [1, 2, 3, 4, 5, 6]
print(primes)

print("Сумма первых двух простых чисел ", primes[0] + primes[1])
primes.append(59)
primes[0] = 100
print(primes)

for i in range(len(primes)):
    print(primes[i])

for x in primes:
    print(x)