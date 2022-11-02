from word import count_word
import unittest

class Test_word(unittest.TestCase):
    def test_number(self):
        res = count_word("Hi how are things? How are you? Are you a developer? I am also a developer")
        print((res))
        self.assertEqual(res, 16)
    def test_int(self):
        res = count_word("1 2 3 4")
        print((res))
        self.assertEqual(res, 4)
    def test_float(self):
        res = count_word("6.5 6.4 5.9")
        print((res))
        self.assertEqual(res, 3)


if __name__=='__main__':
    unittest.main()

    