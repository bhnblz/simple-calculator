import colorama
from colorama import Fore

import pyfiglet
greetings = "Hello!"
print(pyfiglet.figlet_format (greetings.center(60), font = "standard"))
title = "THIS IS A SIMPLE CALCULATOR PROGRAM"
print(Fore.LIGHTRED_EX + "=" * 80)
print(Fore.LIGHTRED_EX + title.center(80))
print("=" * 80)
print("\n")

description = "The purpose of this program is to create a simple calculator that has four operations "
print(Fore.LIGHTYELLOW_EX + description.center(30))
description_2 = "to perform depending on the user's desire, such as addition, subtraction, multiplication, and division."
print(description_2.center(30))
print("\n")
introduction = "My name is Bhea and here's my simple calculator python program."
print(Fore.LIGHTGREEN_EX + introduction.center(30))

def simple_calculator():
    print("\n")
    while True:
        # Ask the user for the operation
        operation = input(Fore.LIGHTWHITE_EX + "What operation do you want to perform? (+, -, *, /): ")
        # Ask the user to input two numbers
        try:
            integer_1 = float(input(Fore.LIGHTCYAN_EX + "Enter first number: "))
            integer_2 = float(input(Fore.LIGHTCYAN_EX + "Enter second number: "))
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
            print(Fore.LIGHTRED_EX + f"\nError: {result}")
            print("\nTry Again")

        # Ask user if they want to continue in solving
        solve_again = input(Fore.LIGHTWHITE_EX + "\nDo you want to solve again? (y/n): ")
        # If yes, continue solving
        if solve_again == "y":
            simple_calculator() 
        # If no, exit the program
        elif solve_again == "n":
            print("Thank you!")
            exit()

# Call the function
simple_calculator()