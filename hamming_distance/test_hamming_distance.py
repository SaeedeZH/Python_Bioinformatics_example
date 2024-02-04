import unittest
from hamming_distance.hamming_distance import hamming_dis
from hamming_distance.hamming_distance import find_pattern

class HammingDistanceTest(unittest.TestCase):
    def test_hamming_dis(self):
        self.assertEqual(1, hamming_dis("abc", "acc"))

    def test_find_pattern(self):
        self.assertEqual(2, find_pattern("abcdefcgf", "cdf",1))
    
# hd = HammingDistanceTest()
# hd.test_find_pattern()
# hd.test_hamming_dis()
if __name__ == '__main__':
    unittest.main()