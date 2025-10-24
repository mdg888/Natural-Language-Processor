from unittest import mock
import unittest
from src.stop_words import *
import pandas as pd

class TestStopWordsRemoval(unittest.TestCase):

   # ------ Conditions Testing ------ #

   def test_empty_string(self):
       # Create fake data input
       data_test = pd.DataFrame({'text': []})  # Empty list, not empty string
       
       # Call the function
       result = remove_stopwords(data_test)
       
       # Test the result
       self.assertEqual(result, [])

   def test_removes_stopwords(self):
       # Create fake data with stopwords
       data_test = pd.DataFrame({'text': [['the', 'cat', 'is', 'here']]})
       
       # Call the function
       result = remove_stopwords(data_test)
       print(result['text'].tolist())
       
       # Test that stopwords are removed (only 'cat' should remain)
       self.assertEqual(result['text'].tolist(), [['cat']])