Balance = 5000                                                      #Initializing certain amount of balance
Hidden_pin = 2003                                                   #setting pin to the account
transaction_history = []                                            #To store the transaction history


def Account_Balance_Inquiry():                                      #It is the function to display the Account Balance Inquiry
    Pin = int(input("Enter the pin number: "))                      #To the every function entering the secret pin to do further process
    if len(str(Pin)) == 4 and Pin == Hidden_pin:                    #Checking the entered pin and the previously setted pin i.e. hidden pin
        print(f'Your Account balance:{Balance}')                    #Displaying the balance
        transaction_history.append('checked balance')
    else:
        print('You Entered Invalid Pin')                            #If you entered the wrong it displays this print statement


def Cash_withdrawal():                                              #function for cash_withdrawal
    global Balance
    Pin = int(input("Enter the pin number: "))
    if len(str(Pin)) == 4 and Pin == Hidden_pin:
        Amount = int(input('Enter the amount: '))                   #Enter the amount to withdraw from the account
        if Amount <= Balance:                                       #if entered amount is less than balance then amount is withdrawn and updates the balance
            Balance -= Amount
            transaction_history.append(f'withdrawn {Amount}')       #undated amount is stored the transaction history to display at the final
        else:
            print('Insufficient funds')                             #if entered amount is greater than the balance it displays insufficient funds
    else:
        print('You Entered Invalid Pin')


def Cash_deposit():                                                 #It is the function for cash_deposit
    global Balance
    Pin = int(input("Enter the pin number: "))
    if len(str(Pin)) == 4 and Pin == Hidden_pin:
        Amount = int(input('Deposit the amount: '))
        Balance += Amount                                           #Adding the entered amount to the balance and updates the balance
        transaction_history.append(f'deposited {Amount}')           #Again the transaction history is stored in the list
    else:
        print('You Entered Invalid Pin')


def Pin_change():                                                   #It is the function for Pin_change
    global Hidden_pin
    Old_pin = int(input('Enter the Old pin: '))                     #Entering the old_pin
    if Old_pin == Hidden_pin:                                       #checking the oldpin with hidden pin if it corrects
        New_pin = int(input("Enter the New Pin: "))                 #then only it will asks for the new pin
        Hidden_pin = New_pin                                        #the new pin is updated to the hidden pin and displays the print statement
        print('Pin successfully changed')
        transaction_history.append(f'pin is changed from old_pin {Old_pin} to new_pin {New_pin}')                   #
                                                                    #the updated pin is stored in the history
    else:
        print('You Entered Wrong Pin')


def Transaction_history():                                          #It is the function to display the transaction history
    Pin = int(input('Enter the ppin number: '))
    if len(str(Pin)) == 4 and Pin == Hidden_pin:
        print('Last Five Transactions')
        for transaction in transaction_history[-5:]:                #This loop will displays the last five transactions
            print(transaction)
        print(f'Your Account Balance: {Balance}')                   #After the transactions it will aslo displays balance amount
    else:
        print('You Entered Invalid Pin')


while True:                                                         #To make it continuously by using while loop
    print("""                                                       #In this statement shows the choise to do specific task
        \n ATM Menu
           1. Account Balance Inquiry
           2. Cash Withdrawal
           3. Cash Deposit
           4. Pin Change
           5. Transaction History
           6. Exit""")
    num = int(input("Choose your option: "))                        #taking the input from the given options
    if num == 1:                                                    #After the entering the choise the appropriate function will calls to the specific task which is assigned
        Account_Balance_Inquiry()
    elif num == 2:
        Cash_withdrawal()
    elif num == 3:
        Cash_deposit()
    elif num == 4:
        Pin_change()
    elif num == 5:
        Transaction_history()
    elif num == 6:                                                  #This choise will exits the loop
        break
    else:
        print("Invalid Option. Please Choose Valid Option.")        #This statement displays to choose correct option
