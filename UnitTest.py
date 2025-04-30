import unittest
from atm_module import ATM



class TestATM(unittest.TestCase):

    def setUp(self):
        # Use an in-memory database for isolated testing
        self.atm = ATM(':memory:')
        self.test_account = '123'
        self.test_pin = '4321'
        self.atm.create_account(self.test_account, self.test_pin)

    def tearDown(self):
        self.atm.close()

    def test_create_account_success(self):
        new_account = '456'
        result = self.atm.create_account(new_account, '1234')
        self.assertTrue(result)
        self.assertTrue(self.atm.account_exists(new_account))

    def test_create_account_duplicate(self):
        result = self.atm.create_account(self.test_account, '0000')
        self.assertFalse(result)

    def test_account_exists(self):
        self.assertTrue(self.atm.account_exists(self.test_account))
        self.assertFalse(self.atm.account_exists('111'))

    def test_verify_pin_correct(self):
        self.assertTrue(self.atm.verify_pin(self.test_account, self.test_pin))

    def test_verify_pin_incorrect(self):
        self.assertFalse(self.atm.verify_pin(self.test_account, '0000'))

    def test_deposit_success(self):
        result = self.atm.deposit(self.test_account, 100.0)
        self.assertTrue(result)
        balance = self.atm.get_balance(self.test_account)
        self.assertEqual(balance, 100.0)

    def test_deposit_invalid_amount(self):
        result = self.atm.deposit(self.test_account, -50.0)
        self.assertFalse(result)

    def test_withdraw_success(self):
        self.atm.deposit(self.test_account, 200.0)
        result = self.atm.withdraw(self.test_account, 150.0)
        self.assertTrue(result)
        balance = self.atm.get_balance(self.test_account)
        self.assertEqual(balance, 50.0)

    def test_withdraw_insufficient_funds(self):
        self.atm.deposit(self.test_account, 50.0)
        result = self.atm.withdraw(self.test_account, 100.0)
        self.assertFalse(result)

    def test_withdraw_invalid_amount(self):
        result = self.atm.withdraw(self.test_account, -20.0)
        self.assertFalse(result)

    def test_get_balance_default(self):
        self.assertEqual(self.atm.get_balance('0000000000'), 0.0)

if __name__ == '_main_':
    unittest.main()
