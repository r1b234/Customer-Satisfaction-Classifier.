import unittest
from classifier import classify_sentiment

class TestSentimentClassifier(unittest.TestCase):
    def test_satisfied(self):
        score, cl = classify_sentiment("Bohot badiya app hai!")
        self.assertEqual(cl, "Satisfied")
        
    def test_dissatisfied(self):
        score, cl = classify_sentiment("Bilkul bakwas service hai.")
        self.assertEqual(cl, "Dissatisfied")

    def test_neutral(self):
        score, cl = classify_sentiment("It is okay, nothing special.")
        self.assertEqual(cl, "Neutral")

if __name__ == '__main__':
    unittest.main()
