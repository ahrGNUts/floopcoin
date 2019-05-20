blockchain = []

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]

def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = 1

    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    return float(input('please enter your transaction amount: '))

def get_user_choice():
    return input('Your choice: ')

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting blocks:')
        print(block)


while True:
    print('Make a selection: ')
    print('1. Add new transaction value')
    print('2. Output the blockchain blocks')
    print('q. Quit')
    choice = get_user_choice()

    if choice == '1':
        tx_amt = get_transaction_value()
        add_transaction(tx_amt, get_last_blockchain_value())
    elif choice == '2':
        print_blockchain_elements()
    elif choice == 'q':
        break
    else:
        print('Invalid. Please make a selection from the list.')

print('Done.')
