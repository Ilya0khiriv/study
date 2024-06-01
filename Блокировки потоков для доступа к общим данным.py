import threading
from threading import Thread


class BankAccount():

    def __init__(self):
        self.balance = 1000

    def deposit(self, money):
        self.balance += money
        print(f"Deposited {money}, new balance is {self.balance}")

    def withdraw(self, money):
        self.balance -= money
        print(f"Withdrew {money}, new balance is {self.balance}")


account = BankAccount()

def deposit_task(account, amount, lock):
    with lock:
        for _ in range(5):
            account.deposit(amount)


def withdraw_task(account, amount, lock):
    with lock:
        for _ in range(5):
            account.withdraw(amount)



lock = threading.Lock()
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100, lock))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150, lock))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
