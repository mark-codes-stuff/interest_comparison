#Script to compare 2 savings interest rates, and format the monthly and annual interest & difference in a table

#Interest and balance variables, including a modified variable which will be used when formatting the original instead of changing it
interest_1 = input("First interest rate, either as a percentage or a decimal \n")
formatted_interest_1 = 0
interest_2 = input("Second interest rate, either as a percentage or a decimal \n")
formatted_interest_2 = 0

balance = input("Balance to calculate against, as a number \n")
formatted_balance = 0

percentage_symbol = "%"
character_to_remove = ['%', '£', '$', '€']
decimal_check = '.'

check_complete = False

#function to validate input and format the strings correctly before turning interests into floats
while check_complete is False:
    for char in character_to_remove: #remove a forbidden character before converting to float
        interest_1 = interest_1.replace(char, '')
        
    for char in character_to_remove: #remove a forbidden character before converting to float
        interest_2 = interest_2.replace(char, '')
        
    while balance.isnumeric() == False: #check the balance is a number and not text
        balance = input("Please re-enter balance as number \n")
    
    for char in character_to_remove:
        balance = balance.replace(char, '')
    


    print(f'Interest 1 = {interest_1}')
    print(f'Interest 2 = {interest_2}')
    print(f'Balance = {balance}')
    check_complete = True


    #Formatting and calculating interest to do later