import unittest

from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")


unittest.main()
