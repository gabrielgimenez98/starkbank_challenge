import unittest
import datetime
from unittest.mock import patch, mock_open
from services.utils import _generate_amount, read_pem_file, generate_end_time, generate_interval, generate_random_invoice_dict, generate_transaction_dict

class TestYourModule(unittest.TestCase):

    def test_generate_amount(self):
        amount = _generate_amount()
        self.assertTrue(0 <= amount <= 100000)

    @patch("builtins.open", mock_open(read_data="mocked pem content"))
    def test_read_pem_file_exists(self):
        pem_content = read_pem_file("test.pem")
        self.assertEqual(pem_content, "mocked pem content")

    def test_read_pem_file_not_exists(self):
        pem_content = read_pem_file("nonexistent.pem")
        self.assertIsNone(pem_content)

    def test_generate_end_time(self):
        end_time = generate_end_time()
        self.assertIsInstance(end_time, datetime.datetime)

    def test_generate_interval(self):
        interval = generate_interval()
        self.assertIsInstance(interval, datetime.timedelta)

    def test_generate_random_invoice_dict(self):
        invoice_dict = generate_random_invoice_dict()
        self.assertIsInstance(invoice_dict, dict)
        self.assertIn("amount", invoice_dict)
        self.assertIn("due", invoice_dict)
        self.assertIn("expiration", invoice_dict)
        self.assertIn("fine", invoice_dict)
        self.assertIn("interest", invoice_dict)
        self.assertIn("tags", invoice_dict)

    def test_generate_transaction_dict(self):
        invoice = {"amount": 100, "id": 12345}
        transaction_dict = generate_transaction_dict(invoice)
        self.assertIsInstance(transaction_dict, dict)
        self.assertIn("amount", transaction_dict)
        self.assertIn("receiver_id", transaction_dict)
        self.assertIn("description", transaction_dict)
        self.assertIn("external_id", transaction_dict)
        self.assertIn("tags", transaction_dict)