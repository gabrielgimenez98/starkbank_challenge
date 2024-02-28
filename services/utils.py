import datetime

import random

def _generate_fine_or_interest() -> float:
    return random.uniform(1, 99)

def _generate_amount() -> int:
    return random.randint(0,100000)

def read_pem_file(file_path):
    try:
        with open(file_path, 'r') as file:
            pem_content = file.read()
        return pem_content
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return None
    
def generate_end_time() -> datetime:
    return datetime.datetime.now() + datetime.timedelta(hours=24)

def generate_interval():
    return datetime.timedelta(hours=3)

def generate_random_invoice_dict() -> dict:
    return {
    "amount": _generate_amount(),
    "name": "Gabriel Gimenez",
    "tax_id": "012.345.678-90",
    "due": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    "expiration": 1000,
    "fine": _generate_fine_or_interest(),
    "interest": _generate_fine_or_interest(),
    "tags": ["scheduled"]
}

def generate_transaction_dict(invoice: dict) -> dict:
    return {
    "amount": invoice["amount"],
    "receiver_id": "6341320293482496",
    "description": "Transaction",
    "external_id": invoice["id"],
    "tags": ["provider"]
}
