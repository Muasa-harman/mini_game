MA_LINES = 3
MA_BET = 1000
MIN_BET = 100

def deposit():
    while True:
        amount = input("What would you like to deposit? Kshs ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print(f"Amount must be between {MIN_BET} - {MA_BET}.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-" + str(MA_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 < lines <= MA_LINES:
                return lines
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")


def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? Kshs ({MIN_BET}, Ma: {MA_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MA_BET:
                return amount
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return get_bet()


def main():    
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
        print(f"You do not have enough amount, your current balance is: {balance}")
    else:
        print(f"You are betting Kshs {bet} on {lines} lines. Total bet is equal to: Kshs {total_bet}")    
    


main()    
                