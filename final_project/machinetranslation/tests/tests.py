import unittest
from translator import english_to_french, french_to_english

class TestTranslateMethods(unittest.TestCase):

    def testEnglishToFrench(self):
        self.assertEqual(english_to_french('Hello'),'Pepitoooo')
        self.assertEqual(english_to_french('Yes'),'Oui')

    def testFrenchToEnglish(self):
        self.assertEqual(french_to_english('vin',),'wine')
        self.assertEqual(french_to_english('moutarde'),'mustard')

if __name__ == '__main__':
    unittest.main()