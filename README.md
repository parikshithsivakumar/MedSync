# MedSync — Secure Medical Records dApp

<p align="center">
  <img alt="MedSync" src="https://img.shields.io/badge/MedSync-Secure%20Records-ED4C97?style=for-the-badge">
  <img alt="Solidity" src="https://img.shields.io/badge/Solidity-%20%20-37474F?style=for-the-badge">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
</p>

A simple proof-of-concept dApp that stores patient medical records on IPFS and manages access via a Solidity `Hospital` smart contract. The project includes a Truffle-based contract, a Python/Gradio frontend, and utilities for uploading `.docx` files to Pinata IPFS.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running Locally](#running-locally)
- [Testing](#testing)
- [Environment & Secrets](#environment--secrets)
- [CI / GitHub Actions](#ci--github-actions)
- [Contributing](#contributing)

---

## Features
- Role-based access control (Patient, Doctor, Lab Technician) implemented in `Hospital.sol`
- Store and retrieve IPFS CIDs for `.docx` medical records
- Gradio-based Python frontend for demo and manual interaction
- Utilities for creating and uploading `.docx` files to Pinata

---

## Tech Stack
- Solidity (0.8.x) + Truffle
- Python 3.9+ (Gradio, web3.py)
- Pinata (IPFS pinning service)
- Ganache for local blockchain testing

---

## Repository Structure
```
.
├── contracts/                 # Solidity contracts
│   └── Hospital.sol
├── migrations/                # Truffle migrations
├── build/                     # Compiled contract artifacts (ignored)
├── frontend/                  # Python Gradio frontend and utilities
│   ├── app.py
│   ├── config.py
│   ├── pinata_utils.py
│   └── word_utils.py
├── test/                      # Truffle tests
├── .github/                   # CI workflows
├── .env.example               # Example env vars (do not commit secrets)
├── requirements.txt
├── package.json
├── README.md
└── LICENSE
```

---

## Prerequisites
- Node.js (16+ recommended) and npm
- Truffle (npm install -g truffle) or use npx
- Python 3.9+
- Ganache CLI or Ganache GUI for local chain

---

## Installation & Setup
1. Clone the repo:
```bash
git clone https://github.com/parikshithsivakumar/MedSync.git
cd MedSync
```

2. Install Node dependencies (for Truffle):
```bash
npm ci
```

3. Install Python dependencies:
```bash
python -m pip install -r requirements.txt
```

4. Create a local `.env` from the example and add secrets:
```bash
cp .env.example .env
# Edit .env and fill PINATA_API_KEY, PINATA_SECRET_API_KEY
```

---

## Running Locally
1. Start Ganache on port 7545 (default):
```bash
npx ganache-cli -p 7545
```

2. Deploy contracts with Truffle (note the deployed address):
```bash
npx truffle migrate --reset --network development
```

3. Set `CONTRACT_ADDRESS` environment variable after deployment (or update `.env`):
```bash
# Replace <deployed_address> with the one from truffle output
export CONTRACT_ADDRESS=<deployed_address>
# On Windows PowerShell:
# $env:CONTRACT_ADDRESS = "<deployed_address>"
```

4. Run the Gradio frontend:
```bash
python -m frontend.app
```

Open the URL printed by Gradio (usually http://127.0.0.1:7860).

---

## Testing
- Run Truffle tests:
```bash
npx truffle test
```

- Python formatting & linting (pre-commit hooks configured):
```bash
python -m pip install pre-commit
pre-commit install
pre-commit run --all-files
```

---

## Environment & Secrets
- Important env vars (see `.env.example`):
  - `PINATA_API_KEY`, `PINATA_SECRET_API_KEY` — Pinata credentials
  - `CONTRACT_ADDRESS` — address of deployed `Hospital` contract
  - `WEB3_PROVIDER` — RPC endpoint (defaults to `http://127.0.0.1:7545`)

- **Do NOT commit secrets.** If secrets were committed previously, rotate them immediately and scrub history (use `git filter-repo` or BFG Repo-Cleaner).

---

## CI / GitHub Actions
A CI workflow runs Truffle tests and a Python lint job on pushes and PRs to `main`. If CI requires secrets (e.g., uploading to Pinata), add them under **Settings → Secrets and variables → Actions**.

---

## Contributing
See `CONTRIBUTING.md` for guidelines. Create small, focused PRs and include tests for non-trivial changes.



