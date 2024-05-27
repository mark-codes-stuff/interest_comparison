#Script to compare 2 savings interest rates and format the monthly and annual interest in a table

interest_1 = input("First interest rate, either as a percentage or a decimal \n")
interest_2 = input("Second interest rate, either as a percentage or a decimal \n")

balance = input("Balance to calculate against, as a number \n")

character_to_remove = ['%', '£', '$', '€']
decimal_check = '.'

check_complete = False

#function to validate input and format the strings correctly before turning interests into floats
#these checks don't currently work as the iteration is wrong, to fix on next look
while check_complete is False:
    for character_to_remove in interest_1: #remove a forbidden character before converting to float
        interest_1 = interest_1.replace(character_to_remove, '')
        
    for character_to_remove in interest_2: #remove a forbidden character before converting to float
        interest_2 = interest_2.replace(character_to_remove, '')
        
    if balance.isnumeric() == False: #check the balance is a number and not text
        balance = input("Please re-enter balance as number \n")
    
    for character_to_remove in balance:
        balance = balance.replace(character_to_remove, '')
    


    print(f'Interest 1 = {interest_1}')
    print(f'Interest 2 = {interest_2}')
    print(f'Balance = {balance}')
    check_complete = True


    #Formatting and calculating interest to do later