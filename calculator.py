quit = "n"
first_no = float(input("Enter the first no.: "))

def operations(first_no, second_no, operation):
    if operation == "+":
        return first_no + second_no
    elif operation == "-":
        return first_no - second_no
    elif operation == "*":
        return first_no * second_no
    elif operation == "/":
        return first_no / second_no
    else:
        return "Your inputed operation is incorrect."

while quit != "y":
    print("+\n-\n*\n/\n")
    operation = input("Enter any operation: ")
    second_no = float(input("Enter your second no.: "))
    result = operations(first_no, second_no, operation)
    print("Result:", result)

    quit = input("Do you want to quit (y/n)? ").lower()
    if quit != "y":
        new = input(f"Type 'y' to continue with {result}, or 'n' to start new: ").lower()
        if new == "y":
            first_no = result
        else:
            first_no = float(input("Enter the first no.: "))
