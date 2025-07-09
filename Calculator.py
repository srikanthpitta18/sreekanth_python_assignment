print("Welcome to the my calculator!")
print("You can enter:")
print("Single operations (for example 4 + 5)")
print("Multiple operations (for example 4 + 5 * 2 - 3 / 1)")
print("Type 'exit' to quit")

while True:
    expression = input("Enter your expression: ")

    if expression.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        result = eval(expression)
        print("Result:", result)

    except ZeroDivisionError:
        print("Result: undefined")
    except Exception:
        print("Invalid expression. Please enter a valid one.")
