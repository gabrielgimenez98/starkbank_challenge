import starkbank
from inputs import Invoice, Transaction

from services.utils import read_pem_file

class StarkBankService():
    def __init__(self) -> None:
        private_key_content = read_pem_file("privateKey.pem")
        starkbank.language = "en-US"
        project = starkbank.Project(
            environment="sandbox",
            id="4814656505905152",
            private_key=private_key_content
        )

        starkbank.user = project

    def create_invoices(invoice_list: list[Invoice]):
        invoices = starkbank.invoice.create(
            invoices=invoice_list
        )

        return invoices
    
    def make_transaction(transaction: Transaction):
        transactions = starkbank.transaction.create(
            transactions=transaction
        )

        return transactions





