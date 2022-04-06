from blockchain import Blockchain

fake_transaction = {"sender": "Bob",
                    "receiver": "Hacker", "amount": "1000000"}

print("\nCOE 817 - Final Project: Blockchain Fundamentals")
print("====================================================\n")

print("A Blockchain is initialized with a genesis block, as can be verified below. \nThe previous hash is all zeros, and the hash is the SHA-256 hash of the block's data. \n")

local_blockchain = Blockchain()
local_blockchain.print_blocks()  # verify genesis block is created

print("\nTo interact with the blockchain, choose from the options below:")

ready = True

while ready:

    print("\n(1) Add a block to the blockchain")
    print("(2) Verify the blockchain")
    print("(3) Print the blockchain")
    print("(4) Add in fraudulent transactions")
    print("(5) Reset the blockchain to the genesis block")
    print("(6) Exit")

    message = input(
        """\nEnter Option: """)

    if message == "1":
        print("The process for adding a block revolves around a transaction. Please enter the following:")

        # Get sender, reciever, and amount
        sender = input("Enter sender: ")
        receiver = input("Enter receiver: ")
        amount = input("Enter amount: ")

        print("\nThis transaction will be encrypted along with the current time, current date, previous hash value and nonce value (which will increase by 1 until the result is met). Together this forms the block header.\n")

        new_transaction = {"sender": sender,
                           "receiver": receiver, "amount": amount}

        local_blockchain.add_block(new_transaction)
        print("\nBlock successfully added to blockchain.")

    elif message == "2":
        local_blockchain.print_blocks()
        local_blockchain.validate_chain()
    elif message == "3":
        local_blockchain.print_blocks()
    elif message == "4":
        if (len(local_blockchain.chain) == 1):
            print(
                "There must be at least one block in the blockchain to add fraudulent transactions.")
        elif (local_blockchain.chain[1].transactions == fake_transaction):
            print("Contents for block 1 have already been altered.")
        else:
            real_block = local_blockchain.chain[1]
            local_blockchain.chain[1].transactions = fake_transaction
            print("\n" + str(fake_transaction))
            print("\nFraudulent transactions added to block 1.")
            local_blockchain.print_blocks()
            local_blockchain.validate_chain()

    elif message == "5":
        local_blockchain = Blockchain()
        print("\nBlockchain has been reset to genesis block.")

    elif message == "6":
        ready = False
    else:
        print("\nPlease enter a valid option.")
