import unittest
from translator import english_to_french, french_to_english

class TestTranslateMethods(unittest.TestCase):

    def testEnglishToFrench(self):
        self.assertEqual(english_to_french('Hi'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Hi')
        self.assertEqual(english_to_french('Yes'),'Oui')
        self.assertNotEqual(english_to_french('Yes'),'No')

    def testFrenchToEnglish(self):
        self.assertEqual(french_to_english('vin',),'wine')
        self.assertNotEqual(french_to_english('vin',),'vino')
        self.assertEqual(french_to_english('moutarde'),'mustard')
        self.assertNotEqual(french_to_english('moutarde',),'moustache')

if __name__ == '__main__':
    unittest.main()