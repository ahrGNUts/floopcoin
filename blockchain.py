blockchain = [[1]]

def add_value(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print(blockchain)


add_value(5.4)
add_value(9.8)
add_value(92)