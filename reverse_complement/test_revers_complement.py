import unittest
from reverse_complement.revers_complement import complement, reverse, reverse_complement

class ReverseComplementTest(unittest.TestCase):
    def test_complemet(self):
        self.assertEqual("ACTGCA", complement("TGACGT"))

    def test_reverse_complement(self):
        self.assertEqual("ACGTCA", reverse_complement("TGACGT"))

    def test_reverse(self):
        self.assertEqual("TGCAGT", reverse("TGACGT"))

if __name__ == '__main__':
    unittest.main()


