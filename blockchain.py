blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    return float(input('please enter your transaction amount: '))

def get_user_choice():
    return input('Your choice: ')

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting blocks:')
        print(block)


tx_amt = get_transaction_value()
add_value(tx_amt)

while True:
    print('Make a selection: ')
    print('1. Add new transaction value')
    print('2. Output the blockchain blocks')
    choice = get_user_choice()

    if choice == '1':
        tx_amt = get_transaction_value()
        add_value(tx_amt, get_last_blockchain_value())
    elif choice == '2':
        print_blockchain_elements()
