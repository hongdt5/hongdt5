import os
import sys
import json
import pprint

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
json_file = os.path.join(current_dir, "bank_accounts.json")

class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(
            f"| {self.account_number:9} | {self.account_name:15} | {self.balance:>15} |")
    @classmethod
    def from_json(cls, json_file):
        accounts = []

        with open(json_file) as file:
            data = json.load(file)

            for item in data:
                accounts.append(cls(**item))

        return accounts
json_accounts = BankAccount.from_json(json_file)

print(f"| {'Number':9} | {'Account Name':15} | {'Balance':15} |")
print(f"|{'-' * 11}|{ '-' * 17 }|{'-' * 17}|")
for account in json_accounts:
    account.display()

print()
