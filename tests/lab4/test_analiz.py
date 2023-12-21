import unittest
from src.lab4.rec import film, users, analiz


class TestRecommended(unittest.TestCase):
    def test_rec(self):
        list_of_films = "films.txt"
        history_file = "users.txt"
        input_data = '2, 4'
        expected_result = 'Дюна'
        actual_result = analiz.recomend(input_data)
        self.assertEqual(actual_result, expected_result)

    def test_rec2(self):
        dict_films = "films.txt"
        history_file = "users.txt"
        input_data = '2, 3'
        expected_result = 'Мстители: Финал'
        actual_result = analiz.recomend(input_data)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
