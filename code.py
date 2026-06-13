import math

addition_count = 0
subtraction_count = 0
multiplication_count = 0
division_count = 0
modulus_count = 0
power_count = 0
sqrt_count = 0
factorial_count = 0
log_count = 0
sine_count = 0
cosine_count = 0
tangent_count = 0
total_calculations = 0

attempts = 3
while attempts > 0:
    password = input("Enter Password: ")
    if password == "1234":
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Wrong Password! Attempts left: {attempts}")
if attempts == 0:
        print("Too many incorrect attempts.")
        exit()

    
while True:
    print("===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Logarithm")
    print("10. Sine")
    print("11. Cosine")
    print("12. Tangent")
    print("13. Statistics")
    print("14. View History")
    print("15. Clear History")
    print("16. Export History")
    print("17. Exit")
    choice = input("Enter your choice: ")
    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
    if choice == '1':
        operator = '+'
        result = num1 + num2
        print(result)
        addition_count += 1
        total_calculations += 1

    elif choice == '2':
        operator = '-'
        result = num1 - num2
        print(result)
        subtraction_count += 1
        total_calculations += 1

    elif choice == '3':
        operator = '*'
        result = num1 * num2
        print(result)
        multiplication_count += 1
        total_calculations += 1

    elif choice == '4':
        if num2 == 0:
            print("cannot divide by zero")
        else:
            operator = '/'
            result = num1 / num2
            print(result)
            history = f"{num1} {operator} {num2} = {result}"
            with open("history.txt", "a") as file:
                file.write(history + "\n")
            division_count += 1
            total_calculations += 1

    elif choice == '5':
        operator = '%'
        result = num1 % num2
        print(result)
        modulus_count += 1
        total_calculations += 1

    elif choice == '6':
        operator = '**'
        result = num1 ** num2
        print(result)
        power_count += 1
        total_calculations += 1

    elif choice == '7':
        num1 = float(input("Enter number: "))
        if num1 < 0:
            print("Cannot find square root of a negative number")
        else:
            result = math.sqrt(num1)
            print(result)
            history = f"√{num1} = {result}"
            with open("history.txt", "a") as file:
                file.write(history + "\n")
            sqrt_count += 1
            total_calculations += 1

    elif choice == '8':
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = math.factorial(num)
            print(f"Factorial of {num} = {result}")
            history = f"{num}! = {result}"
            with open("history.txt", "a") as file:
                file.write(history + "\n")
            factorial_count += 1
            total_calculations += 1

    elif choice == '9':
        num = float(input("Enter a positive number:"))
        if num <= 0:
            print("Logarithm is defined only for positive numbers.")
        else:
            result = math.log10(num)
            print(f"log10({num}) = {result}")
            history = f"log10({num}) = {result}"
            with open("history.txt", "a") as file:
                file.write(history + "\n")
            log_count += 1
            total_calculations += 1

    elif choice == '10':
        angle = float(input("Enter angle in degrees:"))
        radians = math.radians(angle)
        result = math.sin(radians)
        print(f"sin({angle}) = {result}")
        history = f"sin({angle}) = {result}"
        with open("history.txt", "a") as file:
            file.write(history + "\n")
        sine_count += 1
        total_calculations += 1
    
    elif choice == '11':
        angle = float(input("Enter angle in degrees:"))
        radians = math.radians(angle)
        result = math.cos(radians)
        print(f"cos({angle}) = {result}")
        history = f"cos({angle}) = {result}"
        with open("history.txt", "a") as file:
            file.write(history + "\n")
        cosine_count += 1
        total_calculations += 1
    
    elif choice == '12':
        angle = float(input("Enter angle in degrees:"))
        radians = math.radians(angle)
        result = math.tan(radians)
        print(f"tan({angle}) = {result}")
        history = f"tan({angle}) = {result}"
        with open("history.txt", "a") as file:
            file.write(history + "\n")
        tangent_count += 1
        total_calculations += 1
    
    elif choice == '13':
        print("===== STATISTICS =====")
        print("Addition:", addition_count)
        print("Subtraction:", subtraction_count)
        print("Multiplication:", multiplication_count)
        print("Division:", division_count)
        print("Modulus:", modulus_count)
        print("Power:", power_count)
        print("Square Root:", sqrt_count)
        print("Factorial:", factorial_count)
        print("Logarithm:", log_count)
        print("Sine:", sine_count)
        print("Cosine:", cosine_count)
        print("Tangent:", tangent_count)
        print("Total Calculations:", total_calculations)

    elif choice == '14':
        with open("history.txt", "r") as file:
            history = file.read()
        print("\n===== HISTORY =====")
        if history.strip() == "":
            print("No history available.")
        else:
            print(history)

    elif choice == '15':
        with open("history.txt", "w") as file:
            file.write("")
            print("History cleared successfully!")
    
    elif choice == '16':
        with open("history.txt", "r") as file:
            history = file.read()
        with open("exported_history.txt", "w") as export_file:
            export_file.write("===== CALCULATOR DATA =====\n\n")
            export_file.write(history)
        print("History exported successfully!")

    elif  choice == '17':
        print("Exiting...")
        break

    else:
        print("Invalid  choice")

    if choice == '7':
        history = f"√{num1} = {result}"
        with open("history.txt", "a") as file:
            file.write(history + "\n")
            
    elif choice in ['1', '2', '3', '5', '6']:
        history = f"{num1} {operator} {num2} = {result}"
        with open("history.txt", "a") as file:
            file.write(history + "\n")

    