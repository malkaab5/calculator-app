def add(x, y): #  function to add two numbers.
  
    return x + y

def subtract(x, y): # function to subtract two numbers.

    return x - y

def multiply(x, y): # function to multiply two numbers.

    return x * y

def divide(x, y): # function to divide two numbers.
  
    if y == 0:
        return "Error! can not divide by 0" # display error if number is divided by 0
    else:
        return x / y


def calculator():
    print("Calculator App")
    print("Choose an operation to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

  
    user_choice = input("Enter choice [1/2/3/4]: ")   # Ask user for input

    if user_choice in ['1', '2', '3', '4']:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))

        if user_choice == '1':
            print(f"{num_1} + {num_2} = {add(num_1, num_2)}")

        elif user_choice == '2':
            print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")

        elif user_choice == '3':
            print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")

        elif user_choice == '4':
            print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")
    else:
        print("Please enter a valid option.")

if __name__ == "__main__":
    while True:
        calculator()
        # Ask the user if they want to perform another calculation
        again = input("Do you want to perform another operation? (Y/N): ").upper()
        if again != 'Y':
            print("Exiting the calculator.")
            break
