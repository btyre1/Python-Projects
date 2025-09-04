MAX_LINES = 3  # Global Constant
MAX_BET = 500
MIN_BET = 1


def deposit(balance=0):   
    while True:  
        amount = input("\nHow much would you like to deposit? $")   
        if amount.isdigit():   
            amount = int(amount)  
            if amount > 0:  
                balance += amount
                print(f"The deposit was successful! New balance: ${balance}")
                break 
            else:
                print("Amount must be greater than 0.")   
        else: 
            print("Please enter a number.")
    
    return balance


def get_number_of_lines():
    while True:  
        lines = input(f"\nHow many lines would you like to bet on (1-{MAX_LINES})? ")  
        if lines.isdigit():   
            lines = int(lines)  
            if 1 <= lines <= MAX_LINES:  
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
    confirmation = input(f'The bet is ${bet} on {lines} line/lines for a total bet of ${total_bet}. Enter "Y" to confirm or "N" to cancel: ').upper()
    
    return confirmation


def show_menu():
    print("\n🎰 SLOT MACHINE MENU 🎰")
    print("1. Play Slot Machine")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Quit")


def play(balance):
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    if balance >= total_bet:
        confirmation = get_confirmation(bet, lines, total_bet)
        if confirmation == "Y":
            balance -= total_bet
            print(f"Bet placed! ${total_bet} deducted. Remaining balance: ${balance}")
        else:
            print("Bet canceled.")
    else:
        print(f"Insufficient funds. You need ${total_bet}, but you only have ${balance}.")
    
    return balance


def main():
    balance = 0
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            if balance > 0:
                balance = play(balance)
            else:
                print("\nYou don't have any balance. Please deposit first.")
        elif choice == "2":
            print(f"\nYour current balance is: ${balance}")
        elif choice == "3":
            balance = deposit(balance)
        elif choice == "4":
            print("\nThanks for playing! Goodbye.")
            break
        else:
            print("\nInvalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()