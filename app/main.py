import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, timestamp=None):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = json.dumps({
            'index': self.index,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'nonce': self.nonce
        }, sort_keys=True)
        
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty=4):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        print(f"Block mined: {self.hash}")


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, [], '0')

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        new_block = Block(
            len(self.chain), 
            transactions, 
            self.get_latest_block().hash
        )
        new_block.mine_block()  # Optional proof-of-work
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if current block links to previous block correctly
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_blockchain(self):
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"Timestamp: {time.ctime(block.timestamp)}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Current Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
            print("-" * 50)


def main():
    # Create a new blockchain
    blockchain = Blockchain()
    
    while True:
        print("\n--- Blockchain Simulation Menu ---")
        print("1. Add a new block")
        print("2. View blockchain")
        print("3. Validate blockchain")
        print("4. Simulate tampering")
        print("5. Exit")

        # Get user choice
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Switch case equivalent using if-elif
        if choice == 1:
            # Add new block
            transaction = input("Enter transaction details: ")
            blockchain.add_block([transaction])
            print("Block added successfully!")

        elif choice == 2:
            # View blockchain
            blockchain.print_blockchain()

        elif choice == 3:
            # Validate blockchain
            is_valid = blockchain.is_chain_valid()
            print(f"Blockchain Integrity: {'Valid' if is_valid else 'Compromised'}")

        elif choice == 4:
            # Simulate tampering
            print("Tampering with block #1's transactions...")
            blockchain.chain[1].transactions = ["Malicious Transaction"]
            is_valid = blockchain.is_chain_valid()
            print(f"Blockchain Integrity After Tampering: {'Valid' if is_valid else 'Compromised'}")

        elif choice == 5:
            # Exit the program
            print("Exiting Blockchain Simulation. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()