import unittest

from main import Student
class MySortTest(unittest.TestCase):


    def setUp(self):
        self.st = Student(name="Kevin")
   #5   ###
    def test_walk(self):
        for i in range(10): self.st.walk()
        self.assertEqual(self.st.distance, 500, f"Дистанции не равны {self.st.distance} != 500")


    def test_run(self):
        for i in range(10): self.st.run()
        self.assertEqual(self.st.distance, 1000, f"Дистанции не равны {self.st.distance} != 1000")


    def test_race(self):
        self.st_2 = Student(name="Nanthan")

        for i in range(10): self.st.run(), self.st_2.walk()
        self.assertGreater(self.st.distance, self.st_2.distance, f"{self.st} должен преодолеть дистанцию больше, чем {self.st_2}")