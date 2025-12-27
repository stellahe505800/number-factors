
def main_function():
    print("Hello from main_function!")
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

    for i in range(2, number):
        # print(f"Counting: {i}")
        if number % i == 0:
            print(f"{i} is a factor of {number}")

    print("Main function execution completed.")

if __name__ == "__main__":
    main_function()
