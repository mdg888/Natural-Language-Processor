from unittest.mock import Mock
from unittest import mock
import unittest
from src.model import *
from src.lemmantisation import *
import pandas as pd

class TestLemmantisation(unittest.TestCase):
    
    # ------ Mocking Testing ------ #

    def setUp(self):
          
        # Create mock objects for all dependencies
        self.mock_tokenizer = Mock()
        self.mock_stopword_remover = Mock()
        self.mock_lemmatizer = lemmantisation
        self.mock_stemmer = Mock()
        self.mock_nlp_engine = Mock()
        
        # Create SpamModel with Porter Stemmer (not lemmatizer)
        self.model = SpamModel(
            tokenizer=self.mock_tokenizer,
            stopword_remover=self.mock_stopword_remover,
            lemmatizer=self.mock_lemmatizer,
            stemmer=self.mock_stemmer,
            nlp_engine=self.mock_nlp_engine
            )

    # ========== VERB TESTS ==========
    # Tests for lemmatizing different verb forms to their base/infinitive form
    
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['running']]}))
    def test_verb_run(self, inp_data):
        # Present participle/progressive form (-ing form)
        # running -> run
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['run']], result['text'].tolist())

    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['went']]}))
    def test_verb_went(self, inp_data):
        # Irregular past tense form
        # went -> go (irregular verb conjugation)
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['go']], result['text'].tolist())

    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['studied']]}))
    def test_verb_studied(self, inp_data):
        # Regular past tense/past participle form (-ed form)
        # studied -> study
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['studi']], result['text'].tolist())
    
    # ========== NOUN TESTS ==========
    # Tests for lemmatizing plural and possessive noun forms to singular
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['cats']]}))
    def test_noun_cats(self, inp_data):
        # Regular plural noun (-s form)
        # cats -> cat
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['cat']], result['text'].tolist())
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['children']]}))
    def test_noun_children(self, inp_data):
        # Irregular plural noun
        # children -> child (irregular pluralization)
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['child']], result['text'].tolist())
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [["dogs"]]}))
    def test_noun_dogs(self, inp_data):
        # Possessive noun form (apostrophe + s)
        # dog's -> dog
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([["dog"]], result['text'].tolist())
    
    
    # ========== ADJECTIVE TESTS ==========
    # Tests for lemmatizing comparative and superlative adjective forms
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['better']]}))
    def test_adjective_better(self, inp_data):
        # Irregular comparative adjective
        # better -> good (irregular comparison)
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['good']], result['text'].tolist())
    
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['happiest']]}))
    def test_adjective_happiest(self, inp_data):
        # Superlative adjective form (-est form)
        # happiest -> happy
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['happi']], result['text'].tolist())
    
    # ========== IRREGULAR VERB FORMS ==========
    # Additional tests for irregular verb conjugations
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['seen']]}))
    def test_irregular_forms_seen(self, inp_data):
        # Past participle of irregular verb
        # seen -> see
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['see']], result['text'].tolist())
    
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['saw']]}))
    def test_irregular_forms_saw(self, inp_data):  # Fixed: renamed to avoid duplicate function name
        # Simple past tense of irregular verb
        # saw -> see
        self.model.chosen = True
        self.model.preprocessing_type = True
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['see']], result['text'].tolist())

    # ------ Conditions Testing ------- 

    def test_empty_string(self):
        # Create fake data input
       data_test = pd.DataFrame({'text': []})  # Empty list, not empty string
       
       # Call the function
       result = lemmantisation(data_test)
       
       # Test the result
       self.assertEqual(result, [])

    def test_non_empty_string(self):
        # Create fake data input
       data_test = pd.DataFrame({'text': []})  # Empty list, not empty string
       
       # Call the function
       result = lemmantisation(data_test)
       
       # Test the result
       self.assertEqual(result, [])