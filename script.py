from blockchain import Blockchain

block_one_transactions = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
block_two_transactions = {"sender": "Bob", "receiver": "Cole", "amount": "25"}
block_three_transactions = {"sender": "Alice",
                            "receiver": "Cole", "amount": "35"}
fake_transactions = {"sender": "Bob",
                     "receiver": "Cole, Alice", "amount": "25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()  # verify genesis block is created

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
print("After adding 3 transactions in the blockchain:")
local_blockchain.print_blocks()

print("Adding fraudulent transactiosn to the blockchain")
print(fake_transactions)
local_blockchain.chain[2].transactions = fake_transactions

print("After adding fraudulent transactions, validating the blockchain")
local_blockchain.validate_chain()

# TODO: Remove example above and define the User Interface below that allows user to interact with blockchain and print out the results
ready = True

while ready:

    message = input(
        """Enter message to send (enter q to quit): \n""")

    if message == 'q':  # Quit
        ready = False
