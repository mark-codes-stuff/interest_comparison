#Script to compare 2 savings interest rates, and format the monthly and annual interest & differences in a table
#This has a lot of printing for debug purposes, a finished and tidy product could have them commented out ;)
#Long-term to-do: add variable investment length, add optional montly contribution

print("This is a script to compare 2 savings interest rates, and format the monthly and annual interest & differences in a table")

#Initialise some variables that will be used later, to avoid local variable errors
interest_1 = ''
interest_2 = ''
balance = ''
formatted_interest_1 = None
formatted_interest_2 = None
formatted_balance = None

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

#Function to re-prompt the user if there's an issue with validation
def re_prompt():
    global formatted_interest_1, formatted_interest_2, formatted_balance
    while formatted_interest_1 is None:
        interest_1 = input("Please input the first interest rate again, either as a percentage or a decimal \n")
        formatted_interest_1 = check_interest(interest_1, percentage_symbol)
    
    while formatted_interest_2 is None:
        interest_2 = input("Please input the second interest rate again, either as a percentage or a decimal \n")
        formatted_interest_2 = check_interest(interest_2, percentage_symbol)

    while formatted_balance is None:
        balance = input("Please input the balance again, as a number or decimal \n")
        formatted_balance = check_balance(balance, characters_to_remove)

#Function to check response
def response_check(response, variable_to_reset):
    global formatted_interest_1, formatted_interest_2, formatted_balance

    if response in ('No', 'no', 'n'):
        if variable_to_reset == 'formatted_interest_1':
            formatted_interest_1 = None
        elif variable_to_reset == 'formatted_interest_2':
            formatted_interest_2 = None
        elif variable_to_reset == 'formatted_balance':
            formatted_balance = None
        re_prompt()
    else:
        print(f"Response suggests no further action is needed for var {variable_to_reset}")

#Interest and balance input
interest_1 = input("Please input the first interest rate, either as a percentage or a decimal \n")
interest_2 = input("Please input the second interest rate, either as a percentage or a decimal \n")
balance = input("Please input the balance to calculate against, as a number or decimal \n")

#Misc variables for checks
percentage_symbol = "%"
characters_to_remove = ['%', '£', '$', '€']
decimal_check = '.'

#Formatting and converting the strings to floats, check if conversion is incomplete and prompt again if needed
formatted_interest_1 = check_interest(interest_1, percentage_symbol)
formatted_interest_2 = check_interest(interest_2, percentage_symbol)
formatted_balance = check_balance(balance, characters_to_remove)
re_prompt()

print(f"Formatted interest 1 (on initial check): {formatted_interest_1}")
print(f"formatted interest 2 (on initial check): {formatted_interest_2}")
print(f"Formatted balance (on initial check): {formatted_balance}")

#Double check with the user that the given values are correct before continuing
print("Are you happy with the given values below? Please indicate with 'no', or 'n' if there's an issue, and you should be prompted to enter it again, otherwise indicate with 'y'")
response1 = input(f"Interest rate 1: {formatted_interest_1} ({formatted_interest_1 * 100}%) \n")
response2 = input(f"Interest rate 2: {formatted_interest_2} ({formatted_interest_2 * 100}%) \n")
response3 = input(f"Balance: {formatted_balance} \n")

response_check(response1, 'formatted_interest_1')
response_check(response2, 'formatted_interest_2')
response_check(response3, 'formatted_balance')

print(f"Formatted interest 1 (after validation): {formatted_interest_1}")
print(f"formatted interest 2 (after validation): {formatted_interest_2}")
print(f"Formatted balance (after validation): {formatted_balance}")

#Calculating interest to do later


#Formatting the table to do later