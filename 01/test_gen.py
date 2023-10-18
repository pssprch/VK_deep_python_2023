import unittest
from io import StringIO
from generator import search_file


class TestSearchFile(unittest.TestCase):

    def setUp(self):
        self.sample_content = """ Привет всем!
                                  Это простой тестовый файл
                                  Розы красные
                                  Фиалки синие
                                  Я учусь программировать
                                  А роза упала на лапу Азора
                                  Роза цветок
                                  Игра """

    def test_word_present(self):
        results = list(search_file(StringIO(self.sample_content), ["Привет"]))
        self.assertEqual(results, ["Привет всем!"])

    def test_word_absent(self):
        results = list(search_file(StringIO(self.sample_content), ["Слово"]))
        self.assertEqual(results, [])

    def test_similar_word_absent(self):
        results = list(search_file(StringIO(self.sample_content), ["розан"]))
        self.assertEqual(results, [])

    def test_case_insensitivity(self):
        results = list(search_file(StringIO(self.sample_content), ["розы"]))
        self.assertEqual(results, ["Розы красные"])

    def test_exact_word_match(self):
        results = list(search_file(StringIO(self.sample_content), ["красные"]))
        self.assertEqual(results, ["Розы красные"])

    def test_file_object(self):
        with StringIO(self.sample_content) as file_obj:
            results = list(search_file(file_obj, ["Фиалки"]))
            self.assertEqual(results, ["Фиалки синие"])
            
    def test_multiple_matches(self):
        results = list(search_file(StringIO(self.sample_content), ["роза"]))
        self.assertEqual(results, ["А роза упала на лапу Азора", "Роза цветок"])

    def test_case_insensitivity_match(self):
        results = list(search_file(StringIO(self.sample_content), ["ФИАЛКИ"]))
        self.assertEqual(results, ["Фиалки синие"])

    def test_matching_several_filters(self):
        results = list(search_file(StringIO(self.sample_content), ["Привет", "учусь", "файл"]))
        self.assertEqual(results, ["Привет всем!", "Это простой тестовый файл", "Я учусь программировать"])

    def test_complete_line_match(self):
        results = list(search_file(StringIO(self.sample_content), ["игра"]))
        self.assertEqual(results, ["Игра"])

    def test_filters_in_diff_line(self):
        results = list(search_file(StringIO(self.sample_content), ["Привет", "тестовый", "файл"]))
        self.assertEqual(results, ["Привет всем!", "Это простой тестовый файл"])

    def test_partial_filters(self):
        results = list(search_file(StringIO(self.sample_content), ["простой", "тестовый", "файл"]))
        self.assertEqual(results, ["Это простой тестовый файл"])

    def test_all_filters_in_line(self):
        results = list(search_file(StringIO(self.sample_content), ["Фиалки", "синие"]))
        self.assertEqual(results, ["Фиалки синие"])


if __name__ == '__main__':
    unittest.main()
