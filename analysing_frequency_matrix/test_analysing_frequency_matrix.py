
import unittest
from analysing_frequency_matrix import consensus_string_for_most_frequent_base_v1, consensus_string_for_most_frequent_base_v3


class Test_analysing_frequency_matrix(unittest.TestCase):
    def test_consensus_string_for_most_frequent_base_v1(self):
        freq_matrix = [[2, 0, 2],
                [1, 2, 0],
                [0, 1, 0],
                [0, 0, 1]]
        self.assertEquals("ACA", consensus_string_for_most_frequent_base_v1(freq_matrix))
    
    def test_consensus_string_for_most_frequent_base_v3(self):
        freq_matrix_dic = { "A": {0:2, 1:0, 2:1},
                "C": {0:1, 1:0, 2:0},
                "G": {0:0, 1:1, 2:0},
                "T": {0:1, 1:0, 2:2}}
        self.assertEquals("AGT", consensus_string_for_most_frequent_base_v3(freq_matrix_dic))

if __name__== "__main__":
    unittest.main()