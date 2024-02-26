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
    "due": datetime.datetime.now(),
    "expiration": datetime.timedelta(hours=3).total_seconds(),
    "fine": _generate_fine_or_interest(),
    "interest": _generate_fine_or_interest(),
    "tags": ["scheduled"]
}
