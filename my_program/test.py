import unittest
from account import Account
from transaction import validation_pix, validation_ted, validation_doc
from transaction import Transaction


class Testing(unittest.TestCase):
    def test_account(self):
        sender_account = Account('Teste 1', '001', '2222', '000.000.000-00')
        receiver_account = Account('Teste 1', '001', '2222', '000.000.000-00')
        self.assertEqual(sender_account.validate_accounts_for_transfer(
            receiver_account), True, 'Should return true for equal accounts')

    # PIX test
    def test_validation_pix(self):
        self.assertEqual(validation_pix(500), True, 'Should return true for values in limits')

    def test_validation_pix_value_greater_than_limit(self):
        self.assertEqual(validation_pix(50000), False, 'Should return false for value greater than five thousand')

    def test_validation_pix_value_less_than_limit(self):
        self.assertEqual(validation_pix(0), False, 'Should return false for a value less than or equal to zero')

    # TED test
    def test_validation_ted(self):
        self.assertEqual(validation_ted(5000.01), True, 'Should return true for values in limits')

    def test_validation_ted_value_less_than_limit(self):
        self.assertEqual(validation_ted(4000), False, 'Should return false for value less than five thousand')

    def test_validation_pix_value_greater_than_limit(self):
        self.assertEqual(validation_ted(11000), False, 'Should return false for a value greater than ten thousand')

    # DOC test
    def test_validation_doc(self):
        self.assertEqual(validation_doc(10000.01), True, 'Should return true for values in limits')

    def test_validation_doc_value_less_than_limit(self):
        self.assertEqual(validation_doc(4000), False, 'Should return false for value less than ten thousand')

if __name__ == '__main__':
    unittest.main()
