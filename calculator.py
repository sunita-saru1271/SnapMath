print("*****Mini Calculator*****")




def get_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError as error:
        print("\nInvalid number input")
        print(error)
        return None, None


while True:

    print("\nPlease select operation\n" \
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "5. Exit\n")

    # Get two numbers
    num1, num2 = get_two_numbers()

    if num1 is not None and num2 is not None:  # Check if the numbers are valid
        select = int(input("Select operation from 1-5: "))

        if select == 1:
            print(num1, "+", num2, "is", num1 + num2)

        elif select == 2:
            print(num1, "-", num2, "is", num1 - num2)

        elif select == 3:
            print(num1, "*", num2, "is", num1 * num2)

        elif select == 4:
            if num2 != 0:
                print(num1, "/", num2, "is", num1 / num2)
            else:
                print("Cannot divide by zero. Try again.")

        elif select == 5:
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid Operation")

    else:
        print("Invalid input. Please try again.")
