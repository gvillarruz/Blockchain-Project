import datetime
from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) + \
            str(self.previous_hash) + str(self.nonce)
        print(block_header) #to see how the nonce value changes per iteration
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        print("Timestamp:", self.time_stamp)
        print("Transactions:", self.transactions)
        print("Current Hash:", self.generate_hash())
        print("Previous Hash:", self.previous_hash)
