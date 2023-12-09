# CalCode - Calculator in Python 
while(1):
    print("\nCalCode - Calculator\nChoose a operation to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exit")
    choice = int(input("\nEnter your choice (1-6): "))

    # Taking User Input only if choice is not equal to 6
    if(choice != 6):
        num1 = int(input("Enter 1st Number: "))
        num2 = int(input("Enter 2nd Number: "))
    
    # Performing Operations
    if choice == 1:
        add = lambda num1, num2 : num1 + num2
        print(f"\nAddition of {num1} & {num2}: {add(num1, num2)}")

    elif choice == 2:
        sub = lambda num1, num2 : num1 - num2
        print(f"\nSubtraction of {num1} & {num2}: {sub(num1, num2)}")

    elif choice == 3:
        mul = lambda num1, num2 : num1 * num2
        print(f"\nMultiplication of {num1} & {num2}: {mul(num1, num2)}")

    elif choice == 4:
        div = lambda num1, num2 : num1 / num2
        print(f"\nDivision of {num1} & {num2}: {div(num1, num2)}")

    elif choice == 5:
        mod = lambda num1, num2 : num1 % num2
        print(f"\nModulus of {num1} & {num2}: {mod(num1, num2)}")

    elif choice == 6:
        print("\nThank you for using CalCode. Goodbye!\n")
        break
    
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")