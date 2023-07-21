'''translator module containing englishToFrench and frenchToEnglish functions'''
import translator
import unittest

class TestStringMethods(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french("bread"), "pain")
        self.assertEqual(translator.english_to_french("bed"), "lit")

        self.assertNotEqual(translator.english_to_french("printer"), "lampe")
        self.assertNotEqual(translator.english_to_french("container"), "souris")

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english("pain"), "bread")
        self.assertEqual(translator.french_to_english("lit"), "bed")

        self.assertNotEqual(translator.french_to_english("imprimante"), "mouse")
        self.assertNotEqual(translator.french_to_english("conteneur"), "lamp")

unittest.main()
