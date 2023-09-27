import unittest
from unittest.mock import Mock
from pr_mess import SomeModel, predict_message_mood


class TestPredictMessageMood(unittest.TestCase):

    def setUp(self):
        self.model = Mock(spec=SomeModel)

    def test_failure(self):
        self.model.predict.return_value = 0.2
        result = predict_message_mood("Какое-то сообщение 1", self.model)
        self.assertEqual(result, "неуд")

    def test_exc(self):
        self.model.predict.return_value = 0.9
        result = predict_message_mood("Какое-то сообщение 2", self.model)
        self.assertEqual(result, "отл")

    def test_okay(self):
        self.model.predict.return_value = 0.5
        result = predict_message_mood("Какое-то сообщение 3", self.model)
        self.assertEqual(result, "норм")

    def test_custom_thresholds(self):
        self.model.predict.return_value = 0.4
        result = predict_message_mood("Какое-то сообщение 4", self.model, 0.3, 0.5)
        self.assertEqual(result, "норм")

        self.model.predict.return_value = 0.2
        result = predict_message_mood("Какое-то сообщение 1", self.model, 0.3, 0.5)
        self.assertEqual(result, "неуд")

    def test_boundary_values(self):
        self.model.predict.return_value = 0.3
        result = predict_message_mood("Какое-то сообщение 5", self.model)
        self.assertEqual(result, "норм")

        self.model.predict.return_value = 0.8
        result = predict_message_mood("Какое-то сообщение 6", self.model)
        self.assertEqual(result, "норм")


if __name__ == "__main__":
    unittest.main()
