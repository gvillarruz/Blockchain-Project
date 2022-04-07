from block import Block
import datetime


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
        previous_hash = (self.chain[len(self.chain)-1]).hash
        print("Block_header: ", datetime.datetime.now(),
              transactions, previous_hash, "0\n")
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        proof = self.proof_of_work(new_block)
        print("\nBlock added to the chain")
        new_block.print_contents()
        self.chain.append(new_block)
        return proof, new_block

    def validate_chain(self):
        # Genesis block
        print("\nGenesis Block: \n")
        print("Previous hash: \n0")  # should always be 0 to begin with
        print("Current hash: ", self.chain[0].hash, "\n")

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if(current.hash != current.generate_hash()):
                print("Block ", i, ":\n")
                print("Previous hash: ", previous.hash)
                # need this to print the hash with the fake transaction
                print("Current hash: invalid hash, try typing 3 into the terminal \n")

                print(
                    "\nINVALID: The current hash of the block does not equal the generated hash of the block.\n")

                print("Block ", i+1, ":\n")
                print("Previous hash: ", current.hash)
                print("Current hash: ", current.generate_hash(), "\n")
                return False
            if(current.previous_hash != previous.generate_hash()):
                print
                print(
                    "\nINVALID: The previous block's hash does not equal the previous hash value stored in the current block.")
                return False

            print("Block ", i, ":\n")
            print("Previous hash: ", previous.hash)
            print("Current hash: ", current.hash, "\n")

        if(len(self.chain) == 1):
            print(
                "Nothing to verify, the only block for this chain is the genesis block.")
        else:
            print(
                "\nBecause block[i-1]'s current hash corresponds with block[i]'s previous hash, this blockchain is valid. The blocks are linked together.")
        return True

    def proof_of_work(self, block, difficulty=2):
        # TODO: print this process flow add some explanation
        # difficulty is number of 0's ahead of the hash

        proof = block.generate_hash()
        print("\nThe current/unique hash for this block is:", proof, "\n")
        print("In order for the proof of work to be verified, the blockhash must be less than equal to the target hash value set by the network. Difficulty is set to", difficulty, "\n")

        nonceFinal = 0
        while proof[:difficulty] != '0'*difficulty:
            block.nonce += 1  # increment nonce until hash with difficulty is found
            nonceFinal = block.nonce
            proof = block.generate_hash()
            print("Proof generated: ", proof)
        block.nonce = 0
        print("\nFinal nonce value/number of iterations before success:",
              nonceFinal, "\n")
        print("Value of the hash that was verified by the network: ", proof)
        return proof

    def invalidHash(self, transactions):
        previous_hash = (self.chain[0]).hash
        new_block = Block(transactions, previous_hash)
        newHash = new_block.generate_hash()
        return newHash
