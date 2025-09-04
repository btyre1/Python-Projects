MAX_LINES = 3  # Global Constant (constant value)
MAX_BET = 500
MIN_BET = 1


def deposit():   
    while True:  
        amount = input("\nHow much would you like to deposit? $")   
        if amount.isdigit():   
            amount = int(amount)  
            if amount > 0:  
                break 
            else:
                print("Amount must be greater than 0.")   
        else: 
            print("Please enter a number.")
    
    return amount


def get_number_of_lines():
    while True:  
        lines = input("\nHow many lines would you like to bet on (1-" + str(MAX_LINES) + ")? ")  # Instead of just writing "(1-3)" in the string, this makes sure that if we change the number of max_lines, it will also update the string.
        if lines.isdigit():   
            lines = int(lines)  
            if 1 <= lines <= MAX_LINES:  # ^Same thing here
                break 
            else:
                print("Amount must be a valid number.")   
        else: 
            print("Please enter a number.")
    
    return lines


def get_bet():
    while True:  
        amount = input("\nWhat would you like to bet on each line? $")  
        if amount.isdigit():   
            amount = int(amount)  
            if MIN_BET <= amount <= MAX_BET:
                break 
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") 
        else: 
            print("Please enter a number.")
    
    return amount


def get_confirmation(bet, lines, total_bet):
    confirmation = input(f'The bet is ${bet} on {lines} line/lines for a total bet of {total_bet}. If this information is correct and you wish to proceed, enter a "Y" for YES, otherwise enter a "N" for NO. ')
    
    return confirmation


def main():
    while True:
        balance = deposit()
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if balance >= total_bet:
            confirmation = get_confirmation(bet, lines, total_bet)
        else:
            print(f"The total bet amount exceeds your balance, you have insufficient funds. Please enter a valid bet.")

        
        
main()

