def simple_calculator():
    print("\n")
    while True:
        # Ask the user for the operation
        operation = input("What operation do you want to perform? (+, -, *, /): ")
        # Ask the user to input two numbers
        try:
            integer_1 = float(input("Enter first number: "))
            integer_2 = float(input("Enter second number: "))
        except ValueError:
            print("\nError: Invalid number input")
            print("\nTry Again!")
            return
        # If addition
        if operation == "+":
            result = integer_1 + integer_2
            print("Answer: " + str(float(result)))
        # If subtraction
        elif operation == "-":
            result = integer_1 - integer_2
            print("Answer: " + str(float(result)))
        # If multiplication
        elif operation == "*":
            result = integer_1 * integer_2
            print("Answer: " + str(float(result)))
        # If division
        elif operation == "/":
            try:
                result = integer_1 / integer_2
                print("Answer: " + str(float(result)))  
            except ZeroDivisionError:
                print("\nError: Cannot divide by zero")
                print("\nTry Again")
                return
        # If invalid operation
        else:
            result = "Invalid Operation"
            print(f"Result: {result}")

        # Ask user if they want to continue in solving
        solve_again = input("\nDo you want to solve again? (y/n): ")
        # If yes, continue solving
        if solve_again == "y":
            simple_calculator() 
        # If no, exit the program
        elif solve_again == "n":
            print("Thank you! See you later.")
            exit()

# Call the function
simple_calculator()