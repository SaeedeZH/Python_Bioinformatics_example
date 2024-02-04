# if __name__ == "__main__":
#It Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module

import unittest
from compare_efficiency_counting_base import count_v1, count_v2, count_v3, count_v4, count_v5, count_v6, count_v7, count_v8, count_v9, count_v10, count_v11, count_v12

class test_compare_efficeincy(unittest.TestCase):

    def test_compare_efficeincy(self):
        functions = [count_v1, count_v2, count_v3, count_v4, count_v5, count_v6, count_v7, count_v8, count_v9, count_v10, count_v11,
             count_v12]
        for fun in functions:
            self.assertEqual(4, fun("AGTGATCGATT","T") )

   # note: if we need the name of fun for daclaring a msg, fun.__name__ is used! ex. f"{fun.__name} failed"
            
if __name__ == "__main__":
    unittest.main()