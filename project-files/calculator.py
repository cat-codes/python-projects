# Calculation
def calculate(number_1, number_2, operator):
    if operator == "+":
        return number_1 + number_2
    elif operator == "-":
        return number_1 - number_2
    elif operator == "*":
        return number_1 * number_2
    elif operator == "**":
        return number_1 ** number_2
    elif operator == "/":
        return number_1 / number_2
    elif operator == "//":
        return number_1 // number_2
    elif operator == "%":
        return number_1 % number_2
    else:
        print("Error")


# Initialization
def init():
    print("Welcome to calculator.")

    number_1 = int(input("number_1: "))
    operator = input("operator: ")
    number_2 = int(input("number_2: "))

    print(number_1, operator, number_2, "=", calculate(number_1, number_2, operator))


# Initializing the program
init()

# https://www.educative.io/answers/how-to-use-the-inputfunction-in-python-for-math-operations