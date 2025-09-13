import random

MAX_LINES = 3  # Global Constant
MAX_BET = 500
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {       # How mmuch each symbol is worth (multipler)
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines): 
        symbol = columns[0][line]  
        for column in columns:  
            symbol_to_check = column[line]  
            if symbol != symbol_to_check:  
                break  
        else:  
            winnings += values[symbol] * bet 
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols): 
    all_symbols = []  
    for symbol, symbol_count in symbols.items():  
        for _ in range(symbol_count):  
            all_symbols.append(symbol)  

    columns = []  
    for _ in range(cols):  
        column = []  
        current_symbols = all_symbols[:]  
        for _ in range(rows):  
            value = random.choice(current_symbols)  
            current_symbols.remove(value)  
            column.append(value)  

        columns.append(column)  

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):  
        print(" | ".join(col[row] for col in columns))

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
                print("Amount must be a valid number. Try again.")   
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
    confirmation = input(f'The bet is ${bet} on {lines} line/lines for a total bet of ${total_bet}. Enter "Y" to confirm the spin or "N" to cancel: ').upper()
    
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
            print(f"\nBet placed! ${total_bet} deducted. Remaining balance: ${balance}\n")
            slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
            print_slot_machine(slots)
            winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
            balance += winnings
            if winning_lines:
                print(f"\nYou won ${winnings} on lines:", *winning_lines)
                print(f"New balance: ${balance}")
            else:
                print("\nNo winnings this time. Better luck next spin!")
            
        else:
            print("\nBet canceled. Returning to main menu.")
    else:
        print(f"\nInsufficient funds. You need ${total_bet}, but you only have ${balance}.")
    
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
            print(f"\nThanks for playing! You left with ${balance}, goodbye.")
            break
        else:
            print("\nInvalid choice. Please enter an available value (1-4).")


if __name__ == "__main__":
    main()