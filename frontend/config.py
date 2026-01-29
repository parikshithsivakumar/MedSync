import json
import os
from web3 import Web3

# Ganache local blockchain (can be overridden via WEB3_PROVIDER env var)
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER", "http://127.0.0.1:7545")))

# Read contract address from environment variable set after deployment
contract_address = os.getenv("CONTRACT_ADDRESS", "")

# Build the absolute path to Hospital.json
base_dir = os.path.dirname(os.path.abspath(__file__))
artifact_path = os.path.join(base_dir, "..", "build", "contracts", "Hospital.json")

with open(artifact_path, "r") as f:
    contract_json = json.load(f)
    abi = contract_json["abi"]

contract = w3.eth.contract(address=contract_address, abi=abi) 
