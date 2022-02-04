import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(''), '')
        self.assertNotEqual(englishToFrench('Bonjour'), 'help')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')


    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(''), '')
        self.assertNotEqual(frenchToEnglish('Help'), 'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
