from datetime import datetime


class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y").date()
        self.email = email
        self.phone = phone

    def get_info(self):
        print("Tên khách hàng:", self.name)
        print("Ngày sinh:", self.date_of_birth)
        print("Email:", self.email)
        print("Điện thoại:", self.phone)


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = owner
        self.balance = balance                 

    @property
    def account_number(self):
        return self._account_number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn hoặc bằng 0")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError(
                "Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")

    def display(self):
        print("Thông tin tài khoản")
        print("Số tài khoản:", self.account_number)
        self.owner.name
        self.owner.get_info()
        print("Số dư:", self.balance, "vnđ")

class SavingAccount(BankAccount):
    monthly_interest_rate = 0.30

    def calculate_interest(self):
        return self.balance * self.monthly_interest_rate


hong = Customer("Hong beo", "18/12/1989", "hongdt5@onemount.com", "0977895346")

my_account = SavingAccount("4701002004758", hong, 25_000_000)
my_account.display()
print("Số tiền tiết kiệm hàng tháng:",my_account.calculate_interest(),"vnđ")