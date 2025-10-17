# task2.py

def personalized_greeting():
    # Taking input from the user
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Concatenating names
    full_name = f"{first_name} {last_name}"

    # Printing greeting message
    print(f"Hello, {full_name}! Welcome!")

if __name__ == "__main__":
    personalized_greeting()