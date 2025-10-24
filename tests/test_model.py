import unittest
from src.model import SpamModel
from unittest.mock import Mock
import pandas as pd
from unittest import mock

class TestModel(unittest.TestCase):

    # ------ Mocking Testing ------ #

    def setUp(self):
        # Mock dependencies
        self.tokenizer = Mock()
        self.stopword_remover = Mock()
        self.lemmatizer = Mock()
        self.stemmer = Mock()
        self.nlp_engine = Mock()

    def test_model_predict_ham(self):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine  # always returns 0.25
        )
        result = model.classify(0.25)
        self.assertEqual(result, "HAM")

    def test_model_predict_spam(self):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine
        )
        result = model.classify(0.75)
        self.assertEqual(result, "SPAM")

    @mock.patch('src.model.SpamModel.preprocessing', return_value=pd.DataFrame({'text': [['']]}))
    def test_model_predict_no_words_found(self,inp):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine
        )
        model.chosen = True
        result = model.predict(inp)
        self.assertEqual("No Words Found!",result)

    @mock.patch('src.model.SpamModel.preprocessing', return_value=pd.DataFrame({'text': [['hithere']]}))
    def test_model_predict_no_words_with_words_found(self,inp):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine
        )
        model.chosen = True
        result = model.predict(inp)
        self.assertEqual("No Words Found!",result)
    
    # ------ Equivalence Partitioning ------ 
    def test_model_classify_ham(self):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine
        )
        self.assertEqual("HAM", model.classify(0.25))
    
    
    def test_model_classify_spam(self):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine  
        )
        self.assertEqual("SPAM", model.classify(0.75))

    # ------ Boundary Value Analysis ------ 
    
    def test_model_classify_spam_bva_049(self):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine  
        )
        self.assertEqual("HAM", model.classify(0.49))
    
    def test_model_classify_spam_bva_049(self):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine  
        )
        
        self.assertEqual("SPAM", model.classify(0.50))
    
    def test_model_classify_spam_bva_049(self):
        model = SpamModel(
            self.tokenizer,
            self.stopword_remover,
            self.lemmatizer,
            self.stemmer,
            self.nlp_engine
        )
        self.assertEqual("SPAM", model.classify(0.51))