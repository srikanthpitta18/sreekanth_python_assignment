while True:
    file_name = input("Enter the lyrics file name or type 'exit' to quit:")

    if file_name.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        with open(file_name, "r") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if line:
                    print(f"{line_number}. {line.upper()}")
                else:
                    print(f"{line_number}. [Blank Line]")
        break

    except FileNotFoundError:
        print("File not found. Please try again.")
    except Exception as e:
        print("An unexpected error occurred:", e)
