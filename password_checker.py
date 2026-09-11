# ensures the firsts digits of the password start with two non-repeating capital letters
def check_capital_letters(password):
    num_required_capital_letters = 2
    num_actual_capital_letters = 0

    past_char = None

    for i in range(2):
            if password[i].isupper():
                if password[i] == past_char:
                    return False
                num_actual_capital_letters += 1
                past_char = password[i]

    if num_actual_capital_letters == num_required_capital_letters:
        return True
    return False

# makes sure all of the digits in the password add up to an even number
def check_sum_even(password):
    sum_of_digits = 0

    for char in password:
        if char.isdigit():
            sum_of_digits += int(char)

    return sum_of_digits % 2 == 0

# makes sure all of the characters in the password are either letters or numbers
def is_letter_and_number(password):
    for char in password:
        if not char.isalpha():
            if not char.isdigit():
                return False
    return True

# determines if the password meets all of the requirements
def password_checker(password):

    # makes sure the password is exactly 8 characters long
    if len(password) == 8:
        if check_capital_letters(password):
            if check_sum_even(password):
                if is_letter_and_number(password):
                    return True
    
    return False

password = input("Enter a password: ")
print(password_checker(password))