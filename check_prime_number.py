
def main_function():
    print("Hello from main_function!")
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
    is_prime = True # this is a boolean flag to track if the number is prime

    for i in range(2, number):
        # print(f"Counting: {i}")
        if number % i == 0:
            is_prime = False

    if is_prime and number > 1:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main_function()
