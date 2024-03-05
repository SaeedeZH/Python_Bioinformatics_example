# for running test file in command use : python -m unittest    
import unittest
import bio_exam

class TestBioExam(unittest.TestCase):

    def test_reverse_complement2(self):
        self.assertEqual(bio_exam.reverse_complement2("ACTG"), "CAGT", "Not equal!")
        #self.assertEqual(bio_exam.reverse_complement2("CGACTG"), "CAGTCA", "Not equal!")

    def test_gc_content(self):
        self.assertEqual(bio_exam.gc_content("ACTCGCGC"), 75.00, "The GC percentage is not correct!")
    
    def test_parse_fasta(self):
        self.assertEqual(bio_exam.parse_fasta("./data/sample1.fa"), 3)
    
    def test_orfs(self):
        self.assertEqual(bio_exam.orfs("ATGGGATGACCCCCTAAGGGGGTAGTTTTTTTGA"), [(0, 14), (0, 22), (0, 6), (4, 13), (4, 21), (4, 5)] )

if __name__== "__main__":
    unittest.main()
