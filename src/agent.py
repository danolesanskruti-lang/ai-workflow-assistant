def calculator():
    print("\nCalculator")
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == "+":
        print("Answer:", a + b)
    elif op == "-":
        print("Answer:", a - b)
    elif op == "*":
        print("Answer:", a * b)
    elif op == "/":
        if b != 0:
            print("Answer:", a / b)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator.")

def main():
    print("=== Basic AI Agent ===")
    print("1. Calculator")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()