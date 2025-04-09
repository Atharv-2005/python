#prime number
n = int(input("Enter a number: "))
print("Primes up to", n)
for num in range(2, n + 1):
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num)