# 4. Check if a number is Prime
import math

number = int(input("Enter a number: "))  # Take input from the user

if number <= 1:
    print(f"{number} is not a prime number.")
elif number == 2:
    print(f"{number} is a prime number.")
elif number % 2 == 0:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

