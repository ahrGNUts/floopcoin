blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


tx_amt = float(input('please enter your transaction amount: '))
add_value(tx_amt)

tx_amt = float(input('please enter your transaction amount: '))
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amt)

tx_amt = float(input('please enter your transaction amount: '))
add_value(tx_amt, get_last_blockchain_value())

print(blockchain)