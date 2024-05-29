#Script to compare 2 savings interest rates, and format the monthly and annual interest & differences in a table
print("This is a script to compare 2 savings interest rates, and format the monthly and annual interest & differences in a table")

#Function to remove misc characters from input
def remove_characters(input_string, characters_to_remove):
    for char in characters_to_remove:
        input_string = input_string.replace(char, '')
    return input_string

#Function to check if the current value can be converted into a float
def is_number(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        print(f"This is not a valid number: {input_string}")
        return False

#Function to check interest is valid and convert to float, and divide by 100 if initial value was given with a percentage symbol
def check_interest(input_string, percentage_symbol):
    is_percentage = percentage_symbol in input_string
    clean_string = remove_characters(input_string, characters_to_remove)

    if is_number(clean_string) is True:
        interest_float = float_convert(clean_string)
    else:
        print(f"Problem with converting interest to float in the check_interest function")
        return None
    
    if is_percentage is True:
        interest_float = (interest_float / 100)

    return interest_float

#Function to check balance is valid and convert to a float
def check_balance(input_string, characters_to_remove):
    clean_string = remove_characters(input_string, characters_to_remove)

    if is_number(clean_string) is True:
        balance_float = float_convert(clean_string)
    else:
        print(f"Problem with converting balance to float in the check_balance function")
        return None
    
    return balance_float

#Function to convert input to float
def float_convert(input_string):
    try:
        new_float = float(input_string)
        return new_float
    except ValueError:
        print(f"There was a problem converting {input_string} into a float in the float_convert function")


#Interest and balance input
interest_1 = input("Please input the first interest rate, either as a percentage or a decimal \n")
interest_2 = input("Please input the second interest rate, either as a percentage or a decimal \n")
balance = input("Please input the balance to calculate against, as a number or decimal \n")

#Misc variables for checks
percentage_symbol = "%"
characters_to_remove = ['%', '£', '$', '€']
decimal_check = '.'

#Formatting and converting the strings to floats, can be printed after to make sure they're correct
formatted_interest_1 = check_interest(interest_1, percentage_symbol)
formatted_interest_2 = check_interest(interest_2, percentage_symbol)
formatted_balance = check_balance(balance, characters_to_remove)

print(f"Formatted interest 1: {formatted_interest_1}")
print(f"formatted interest 2: {formatted_interest_2}")
print(f"Formatted balance: {formatted_balance}")

#Calculating interest to do later
