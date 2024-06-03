import threading
import time

class Table():
    def __init__(self, number, is_busy=False):
        self.number = number
        self.is_busy = is_busy

class Cafe():
    def __init__(self, tables):
        self.queue = [Customer(i) for i in range(1, 21)]
        self.tables = tables

    def next_table(self):
        for table in self.tables:
            if not table.is_busy:
                return table

    def customer_arrival(self):
        lock = threading.Lock()
        while self.queue != []:
            time.sleep(1)
            customer = self.queue[0]
            r = threading.Thread(target=self.serve_customer, args=(customer, lock))
            r.start()
            self.queue.remove(customer)

    def serve_customer(self, customer, lock):

        lock.acquire()
        print(f"Посетитель номер {customer.id} прибыл.", flush=True)

        if self.next_table() is None:
            print(f"Посетитель номер {customer.id} ожидает свободный стол", flush=True)
            while self.next_table() is None:
                time.sleep(0.01)

        table = self.next_table()

        table.is_busy = True
        print(f"Посетитель номер {customer.id} сел за стол {table.number}", flush=True)
        lock.release()
        time.sleep(5)
        print(f"Посетитель номер {customer.id} покушал и ушёл.", flush=True)
        table.is_busy = False


class Customer():
    def __init__(self, id=0):
        self.id = id


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()