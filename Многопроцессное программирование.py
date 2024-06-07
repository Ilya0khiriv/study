import multiprocessing
import time
from multiprocessing import Queue


class WarehouseManager():

    def __init__(self):
        self.data = {}

    def run(self, requests):
        wait_line = Queue(maxsize=1)
        users = []

        multi_user = [multiprocessing.Process(target=self.process_request, args=(request, wait_line), ) for request in requests]
        for process in multi_user:
            users.append(process)
            process.start()


        while True:
            try:
                dict, action = wait_line.get(timeout=1)
                key = list(dict.keys())[0]
                val = list(dict.values())[0]

                if action == "-": val = 0 - val

                if key not in self.data: self.data[key] = val
                elif key in self.data: self.data[key] = self.data[key] + val
            except: pass

            if not any (user.is_alive() for user in multi_user): break

        for user in multi_user: user.join()

    def process_request(self, *args):
        req_, wait_line = args
        product, action, amount = req_

        dict = None
        if action == "shipment":
            dict = {product: amount}, "-"

        if action == "receipt":
            dict = {product: amount}, "+"

        wait_line.put(dict)



if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)
