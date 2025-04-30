import sqlite3
import logging
import bcrypt

logging.basicConfig(
      filename='atm_transactions.log',
      level=logging.INFO,
      format='%(asctime)s - %(levelname)s - %(message)s',

)
class ATM:
    def __init__(self,db_name='test.db'):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
        self._create_account_table()
    def _create_account_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts(
            account_number TEXT PRIMARY KEY,
            balance REAL DEFAULT 0.0,
            pin TEXT NOT NULL
            )
        ''')
        self.conn.commit()


    def create_account(self,account_number,pin):
           if self.account_exists(account_number):
               logging.warning(f"Account creation failed {account_number} already exists.")
               return False
           hashed_pin=bcrypt.hashpw(pin.encode('utf-8'),bcrypt.gensalt())
           self.cursor.execute(
               'INSERT INTO accounts (account_number, pin, balance) VALUES (?,?,?)',
         (account_number, hashed_pin, 0.0)
           )
           self.conn.commit()
           logging.info(f"Account Created: {account_number}")
           return True
    def account_exists(self,account_number):
     self.cursor.execute('SELECT account_number FROM accounts WHERE account_number = ?',(account_number,))
     return self.cursor.fetchone() is not None


    def verify_pin(self,account_number,entered_pin):
        self.cursor.execute(
            "SELECT pin FROM accounts WHERE account_number=?",
            (account_number,)
        )
        result=self.cursor.fetchone()
        if result:
            stored_hashed_pin=result[0]
            if  bcrypt.checkpw(entered_pin.encode('utf-8'),stored_hashed_pin):
                return True
            else:
                logging.warning(f"Incorrect PIN attempt for account{account_number}")
                return False
        else:
            logging.warning(f"Login attempt for non-existent account{account_number}")
            return False

    def get_balance(self,account_number):
        self.cursor.execute(
            'SELECT balance FROM accounts WHERE account_number=?',
            (account_number,)
        )
        result=self.cursor.fetchone()
        if result:
            return result[0]
        return 0.0
    def deposit(self,account_number,amount):
        if amount <= 0:
            return False
        balance=self.get_balance(account_number)
        new_balance=balance+amount
        self.cursor.execute(
            "UPDATE accounts SET balance =? WHERE account_number=?",
            (new_balance,account_number)
        )
        self.conn.commit()
        logging.info(f'Deposited {amount:.2f} to account {account_number}')
        return True
    def withdraw(self,account_number,amount):
        balance=self.get_balance(account_number)
        if amount <= 0 or amount > balance:
            return False
        new_balance=balance-amount
        self.cursor.execute(
            'UPDATE accounts SET balance=? WHERE account_number=? ',
            (new_balance,account_number)
        )
        self.conn.commit()
        logging.info(f'Withdraw {amount:.2f} from account {account_number}')
        return True

    def close(self):
         self.conn.close()