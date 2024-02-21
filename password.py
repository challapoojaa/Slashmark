import random

def generate_password(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = "".join(random.choice(alphabet) for _ in range(length))
    password = replace_with_number(password)
    password = replace_with_uppercase_letter(password)
    return password

def replace_with_number(password):
    for _ in range(random.randint(1, 3)):
        replace_index = random.randint(0, len(password)//2 - 1)
        password = password[:replace_index] + str(random.randint(0, 9)) + password[replace_index + 1:]
    return password

def replace_with_uppercase_letter(password):
    for _ in range(random.randint(1, 3)):
        replace_index = random.randint(len(password)//2, len(password) - 1)
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")

    print("Minimum length of password should be 3")
    
    passwords = [generate_password(max(int(input(f"Enter the length of Password #{i + 1}: ")), 3)) for i in range(num_passwords)]

    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i} = {password}")

if __name__ == "__main__":
    main()
