from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)
        return self.chain

    # prints contents of blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("\nBlock {} {}".format(i, current_block))
            current_block.print_contents()

    def add_block(self, transactions):
        #TODO: print this process flow

        previous_hash = (self.chain[len(self.chain)-1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block

    def validate_chain(self):
         #TODO: print this process flow for each comparison

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if(current.hash != current.generate_hash()):
                print(
                    "\nINVALID: The current hash of the block does not equal the generated hash of the block.")
                return False
            if(current.previous_hash != previous.generate_hash()):
                print(
                    "\nINVALID: The previous block's hash does not equal the previous hash value stored in the current block.")
                return False

        print("\nThe blockchain is valid.")
        return True

    def proof_of_work(self, block, difficulty=2):
        #TODO: print this process flow add some explanation

        proof = block.generate_hash()
        while proof[:difficulty] != '0'*difficulty:
            block.nonce += 1  # increment nonce until hash with difficulty is found
            proof = block.generate_hash()
        block.nonce = 0
        return proof
