import hashlib
import datetime

# Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()


# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            timestamp=datetime.datetime.now(),
            data=data,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("-" * 50)


# Create blockchain
my_blockchain = Blockchain()

# Add blocks
my_blockchain.add_block("Block 1 Data")
my_blockchain.add_block("Block 2 Data")
my_blockchain.add_block("Block 3 Data")
my_blockchain.add_block("Block 4 Data")

print("Original Blockchain:\n")
my_blockchain.display_chain()

# Modify block data
print("\nAfter modifying Block 2 data:\n")
my_blockchain.chain[2].data = "Hacked Data"
my_blockchain.chain[2].hash = my_blockchain.chain[2].calculate_hash()

my_blockchain.display_chain()