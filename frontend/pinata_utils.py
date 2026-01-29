import requests
import os

PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")
if not PINATA_API_KEY or not PINATA_SECRET_API_KEY:
    raise EnvironmentError("Missing PINATA_API_KEY or PINATA_SECRET_API_KEY environment variables")


def upload_to_pinata(filepath):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }
    with open(filepath, 'rb') as file:
        response = requests.post(url, files={"file": file}, headers=headers)
    return response.json()["IpfsHash"]
