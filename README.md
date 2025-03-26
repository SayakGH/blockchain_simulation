# Blockchain Simulation

## 📌 Project Overview

This is a simple, educational Python-based blockchain simulation that demonstrates core blockchain concepts through an interactive command-line application. The project provides a hands-on approach to understanding how blockchains work, including block creation, mining, and integrity validation.

## ✨ Features

- **Interactive CLI Menu**
  - Add new blocks with custom transactions
  - View entire blockchain
  - Validate blockchain integrity
  - Simulate blockchain tampering

- **Technical Blockchain Concepts**
  - Block structure with hash linking
  - SHA-256 cryptographic hashing
  - Proof-of-Work mechanism
  - Chain integrity validation

## 🛠 Prerequisites

- Python 3.7+
- Docker (optional, for containerized deployment)
   though causing a little issue

## 🚀 Installation

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SayakGH/blockchain_simulation.git
   cd blockchain_simulation
   ```

2. Run the application:
   ```bash
   cd app
   python3 main.py
   ```

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t blocksim .
   ```

2. Run the Docker container:
   ```bash
   docker run -it blocksim
   ```

## 🎮 Usage

When you run the application, you'll see a menu with the following options:

1. **Add a new block**
   - Enter a transaction to create a new block
   - Demonstrates block creation and mining process

2. **View blockchain**
   - Displays details of all blocks in the chain
   - Shows block index, timestamp, transactions, and hashes

3. **Validate blockchain**
   - Checks the integrity of the entire blockchain
   - Verifies hash connections between blocks

4. **Simulate tampering**
   - Demonstrates blockchain's resistance to data manipulation
   - Modifies a block and shows how validation fails

5. **Exit**
   - Closes the application

## 🔍 How It Works

### Block Structure
- Each block contains:
  - Block index
  - Transactions
  - Timestamp
  - Previous block's hash
  - Current block's hash
  - Nonce (for Proof-of-Work)

### Proof-of-Work
- Blocks are "mined" by finding a hash with a specific number of leading zeros
- Increases computational difficulty of block creation

### Integrity Validation
- Checks that each block's hash is correctly calculated
- Ensures blocks are linked correctly in the chain

## 🧪 Technical Details

- **Hashing Algorithm**: SHA-256
- **Mining Difficulty**: Configurable (default: 4 leading zeros)
- **No External Dependencies**: Uses only Python standard library

## 🚧 Limitations

- In-memory blockchain (not persistent)
- Simplified blockchain model
- No actual cryptocurrency functionality
