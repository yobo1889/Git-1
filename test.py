import unittest
import project

class TestSOMETHING(unittest.TestCase):
    def test_approval(self):
        self.assertEqual(test("14 WEST ADMINISTRATIVE SVCS LLC"),"0");
        self.assertEqual(test("0 NORTH AVE WAKEFIELD LLC"),"1");
    def test_denial(self):
        self.assertEqual(test("7CINFO COM INC"),"1");
        self.assertEqual(test("ACORNS GROW INCORPORATED"),"0");
if __name__ == '__main__':
      unittest.main()