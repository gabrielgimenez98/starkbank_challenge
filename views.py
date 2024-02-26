import datetime
import time
from fastapi import FastAPI
from inputs import Invoice
from services.starkbank_service import StarkBankService
from services.utils import generate_end_time, generate_interval



app = FastAPI()

@app.post("/invoices")
def generate_invoices():

    print("Iniciando em:", datetime.datetime.now())

    end_time = generate_end_time()

    interval = generate_interval()

    while datetime.datetime.now() < end_time:
        

        time.sleep(interval.total_seconds())

    print("Terminado em:", datetime.datetime.now())

@app.post("/transaction")
def generate_transaction(request: Invoice):

    payload = request.json()
    starkbank_service = StarkBankService()
    starkbank_service.make_transaction(payload)

    
