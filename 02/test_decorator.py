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

    def test_two_calls(self):
        start = time.time()
        self.sleep_half_second()
        first_call = time.time() - start
        start = time.time()
        self.sleep_half_second()
        second_call = time.time() - start
        exp_av = (first_call + second_call) / 2
        self.assertAlmostEqual(first_call, 0.5, delta=0.05)
        self.assertAlmostEqual(second_call, 0.5, delta=0.05)
        self.assertAlmostEqual(exp_av, 0.5, delta=0.05)

    def test_three_calls(self):
        ds = []
        for _ in range(3):
            start = time.time()
            self.sleep_one_second()
            ds.append(time.time() - start)
        exp_av = sum(ds) / 3
        for duration in ds:
            self.assertAlmostEqual(duration, 1, delta=0.05)
        self.assertAlmostEqual(exp_av, 1, delta=0.05)

if __name__ == '__main__':
    unittest.main()
