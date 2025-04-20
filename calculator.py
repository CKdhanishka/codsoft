def display_instructions():
    print("🔢 Simple Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("Type 'exit' to quit.\n")

def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'exit':
                return 'exit'
            return float(value)
        except ValueError:
            print("❗ Invalid input. Please enter a number.")

def get_operation():
    while True:
        op = input("Choose operation (+, -, *, /): ")
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("❗ Invalid operation. Try again.")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "❌ Cannot divide by zero!"
        return num1 / num2

def main():
    display_instructions()
    
    while True:
        num1 = get_number("Enter first number: ")
        if num1 == 'exit':
            break
        num2 = get_number("Enter second number: ")
        if num2 == 'exit':
            break
        operation = get_operation()
        
        result = calculate(num1, num2, operation)
        print(f"\n✅ Result: {num1} {operation} {num2} = {result}\n")

        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()