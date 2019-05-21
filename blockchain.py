blockchain = []
open_transactions = []
owner = 'Me'

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]

def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)



def mine_block():
    pass

def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Please enter your transaction amount: '))
    return tx_recipient, tx_amount

def get_user_choice():
    return input('Your choice: ')

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting blocks:')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 11

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
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
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
