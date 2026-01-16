

def is_prime_number(number) -> bool:
    for i in range(2, int(number/2)+1):
        print(f"try {number}/{i}")
        if number % i == 0:
            print(f"{number} is divisible by {i}, so it is not a prime number.")
            return False
    print(f"{number} is a prime number.")
    return True



def main_function():
    print("Find all prime numbers up to a given number.")
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

    for num in range(2, number + 1):
        if is_prime_number(num):
            print(f"======= {num} =======")


if __name__ == "__main__":
    main_function()
