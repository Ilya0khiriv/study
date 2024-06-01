import threading
import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def _case(self, str_, num):
        dict = {"день": ["день", "дня", "дней"],
                "воин": ["воин", "воина", "воинов"]}

        if str(num)[-1] in ["1"]: return dict[str_][0]
        elif str(num)[-1] in ["2", "3", "4"]: return dict[str_][1]
        elif str(num)[-1] in ["5", "6", "7", "8", "9", "0"]: return dict[str_][2]

    def run(self):
        enemies = 100
        defend_time = 20 / self.skill * 5
        print(f"{self.name}, на нас напали!", flush=True)
        day = 0


        while enemies > 0:
            day += 1

            time.sleep(defend_time)
            enemies -= self.skill
            if enemies < 0: enemies = 0

            print(f"{self.name}, сражается {day} {self._case('день', day)} ..., осталось {enemies} {self._case('воин', enemies)}.", flush=True)

        _day_case = self._case("день", day)
        print(f"{self.name} одержал победу спустя {day} {self._case('день', day)}!", flush=True)


knight1 = Knight("Sir Lancelot", 20) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 10) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print("Все битвы закончились")