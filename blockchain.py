MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Me'
participants = {'Me'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    open_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    return True


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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

waiting_for_input = True;

while waiting_for_input:
    print('Make a selection: ')
    print('1. Add new transaction value')
    print('2. Mine a new block')
    print('3. Output the blockchain blocks')
    print('4. Output participants')
    print('h. Manipulate the blockchain')
    print('q. Quit')
    choice = get_user_choice()

    if choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif choice == '2':
        if mine_block():
            open_transactions = []
    elif choice == '3':
        print_blockchain_elements()
    elif choice == '4':
        print(participants)
    elif choice == 'q':
        waiting_for_input = False
    elif choice == 'h':
        if len(blockchain) > 0:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Me', 'amount': 100}]
            }
    else:
        print('Invalid. Please make a selection from the list.')

    if not verify_chain():
        print('Invalid blockchain')
        break
    print(get_balance('Me'))

print('Done.')
