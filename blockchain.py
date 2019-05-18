blockchain = [[1]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])


add_value(5.4)
add_value(9.8)
add_value(92)

print(blockchain)