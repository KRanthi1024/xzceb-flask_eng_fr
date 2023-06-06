from translator import english_to_french, french_to_english
import unittest

class Test_english_to_french(unittest.TestCase):
    def test1(self):
        actual = english_to_french('hello')
        expected = 'bonjour'
        self.assertEqual(actual, expected) #test when the string 'Hello' is given as input, the output should be 'Bonjour'.

    def test2(self):
        actual_1 = english_to_french('dog')
        expected_1 = 'chat'
        self.assertNotEqual(actual_1, expected_1) #test when the string 'dog' is given as input, the output should not be 'chat'.   

class Test_french_to_english(unittest.TestCase):
    def test3(self):
        actual_3 = french_to_english('bonjour')
        expected_3 = 'hello'
        self.assertEqual(actual_3, expected_3) # test when the string 'Bonjour' is given as input, the output should be 'Hello'.

    def test4(self):
        actual_4 = french_to_english('chien')
        expected_4 = 'cat'
        self.assertNotEqual(actual_4, expected_4) #test when the string 'Chien" is given as input, the output should not be 'dog'.       

if __name__=='__main__':
    unittest.main()
