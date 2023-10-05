import unittest
import time
from decorator import mean

class TestMeanDecorator(unittest.TestCase):

    @mean(2)
    def sleep_half_second(self):
        time.sleep(0.5)
        return True

    @mean(3)
    def sleep_one_second(self):
        time.sleep(1)
        return True

    def test_average_time_two_calls(self):
        start = time.time()
        self.sleep_half_second()
        first_call_duration = time.time() - start
        start = time.time()
        self.sleep_half_second()
        second_call_duration = time.time() - start
        expected_average = (first_call_duration + second_call_duration) / 2
        self.assertAlmostEqual(first_call_duration, 0.5, delta=0.05)
        self.assertAlmostEqual(second_call_duration, 0.5, delta=0.05)
        self.assertAlmostEqual(expected_average, 0.5, delta=0.05)

    def test_average_time_for_three_calls(self):
        durations = []
        for _ in range(3):
            start = time.time()
            self.sleep_one_second()
            durations.append(time.time() - start)
        exp_av = sum(durations) / 3
        for duration in durations:
            self.assertAlmostEqual(duration, 1, delta=0.05)
        self.assertAlmostEqual(exp_av, 1, delta=0.05)

if __name__ == '__main__':
    unittest.main()
