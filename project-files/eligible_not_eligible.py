positive_answer = "yes"
answer = input("Would you like to verify eligibility? ").lower()

while answer == positive_answer:
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    full_name = first_name + " " + last_name
    year_of_birth = input("What is your birth year? ")
    age = (2023 - int(year_of_birth))
    print("Your age is", age)
    print("Your name has", len(full_name) - 1, "characters")

    if age >= 18 and age < 65:
        print(full_name, "is eligible.")
    elif age < 18:
        print(full_name, "is too young, therefore not eligible.")
    else:
        print (full_name, "is too old, therefore not eligible.")

    answer = input("Would you like to verify eligibility again? ").lower()