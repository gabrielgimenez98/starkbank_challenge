import datetime
import random
import time
from fastapi import FastAPI
from inputs import Invoice
from services.starkbank_service import StarkBankService
from services.utils import generate_end_time, generate_interval, generate_random_invoice_dict, generate_transaction_dict



app = FastAPI()

@app.post("/invoices")
def generate_invoices():

    print("Iniciando em:", datetime.datetime.now())

    end_time = generate_end_time()

    interval = generate_interval()

    while datetime.datetime.now() < end_time:
        invoices = []
        for _ in range(random.randint(8,12)):
            invoice = generate_random_invoice_dict()
            invoices.append(invoice)
            print("invoice gerada ",invoice)

        starkbank_service = StarkBankService()
        starkbank_service.create_invoices(invoices)
        

        time.sleep(interval.total_seconds())

    print("Terminado em:", datetime.datetime.now())

@app.post("/transaction")
def generate_transaction(request: dict):

    payload = request["event"]["log"]["invoice"]
    print(payload)
    starkbank_service = StarkBankService()
    print("invoice a ser transferida ",payload)
    random.randint(1,2)
    transaction = generate_transaction_dict(payload)
    response = starkbank_service.make_transaction(transaction)

    return response, 200

    
