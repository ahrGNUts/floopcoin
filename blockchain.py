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

def verify_chain():
    block_index = 0
    is_valid = True

    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid

waiting_for_input = True;

while waiting_for_input:
    print('Make a selection: ')
    print('1. Add new transaction value')
    print('2. Output the blockchain blocks')
    print('h. Manipulate the blockchain')
    print('q. Quit')
    choice = get_user_choice()

    if choice == '1':
        tx_amt = get_transaction_value()
        add_transaction(tx_amt, get_last_blockchain_value())
    elif choice == '2':
        print_blockchain_elements()
    elif choice == 'q':
        waiting_for_input = False
    elif choice == 'h':
        if len(blockchain) > 0:
            blockchain[0] = [2]
    else:
        print('Invalid. Please make a selection from the list.')

    if not verify_chain():
        print('Invalid blockchain')
        break

print('Done.')
