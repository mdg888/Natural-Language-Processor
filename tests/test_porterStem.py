import unittest
from unittest.mock import Mock
from unittest import mock 
from src.model import *
from src.porter_stemmer import *
import pandas as pd

class TestPorterStem(unittest.TestCase):
    
    # ------ Mocking Testing ------ #

    def setUp(self):
          
        # Create mock objects for all dependencies
        self.mock_tokenizer = Mock()
        self.mock_stopword_remover = Mock()
        self.mock_lemmatizer = Mock()
        self.mock_stemmer = run_porter
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
    # Tests that verify verbs are stemmed to their base form
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['running']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_verb_run(self,inp_data,ask_user):
        # Set preprocessing_type to False for stemming
        # User inputs "running", expects stem "runn" 
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['runn']], result['text'].tolist())

    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['hopping']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_verb_hopping(self, inp_data, ask_user):
        # User inputs "hopping", expects stem "hop"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['hopp']], result['text'].tolist())

    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['studied']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_verb_studied(self, inp_data, ask_user):
        # User inputs "studied", expects stem "studi"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['studi']], result['text'].tolist())

    # ========== NOUN TESTS ==========
    # Tests that verify plural nouns are stemmed to their singular form
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['caresses']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_noun_caresses(self, inp_data, ask_user):
        # User inputs "caresses", expects stem "caress"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['caress']], result['text'].tolist())

    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['ponies']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_noun_ponies(self, inp_data, ask_user):
        # User inputs "ponies", expects stem "poni"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['poni']], result['text'].tolist())

    
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['cats']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_noun_cats(self, inp_data, ask_user):
        # User inputs "cats", expects stem "cat"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['cat']], result['text'].tolist())

    # ========== ADJECTIVE TESTS ==========
    # Tests that verify adjectives are stemmed to their base form

    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['relational']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_adjective_relational(self, inp_data, ask_user):
        # User inputs "relational", expects stem "relat"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['relat']], result['text'].tolist())

    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['rational']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_adjective_rational(self, inp_data, ask_user):
        # User inputs "rational", expects stem "ration"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['ration']], result['text'].tolist())

    
    # ========== ADVERB TESTS ==========
    # Tests that verify adverbs and comparatives are stemmed to their base form

    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['better']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_adverb_better(self, inp_data, ask_user):
        # User inputs "better", expects stem "good"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['better']], result['text'].tolist())
    
    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['happiest']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_adverb_happiest(self, inp_data, ask_user):
        # User inputs "happiest", expects stem "happy"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['happi']], result['text'].tolist())
    
    
    # ========== IRREGULAR VERB FORMS ==========
    # Tests that verify irregular verbs are stemmed correctly

    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['seen']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_irregular_verb_seen(self, inp_data, ask_user):
        # User inputs "seen", expects stem "see"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['seen']], result['text'].tolist())


    # ========== AGENT NOUN TESTS ==========
    # Tests that verify agent nouns (words ending in -izer/-iser) are stemmed to their base form

    @mock.patch('src.model.SpamModel.clean_data', return_value=pd.DataFrame({'text': [['digitizer']]}))
    @mock.patch('src.model.SpamModel.apply_preprocessing', return_value='2')
    def test_agent_noun_digitizer(self, inp_data, ask_user):
        # User inputs "digitizer", expects stem "digit"
        result = self.model.preprocessing(inp_data)
        self.assertEqual([['digit']], result['text'].tolist())


    # ------ Conditions Testing ------ #

    def test_empty_string(self):
        # testing for empty string
        # Create fake data input
        data_test = pd.DataFrame({'text': [['the', 'cats', 'there', 'here']]})
       
        # Call the function
        result = run_porter(data_test)
        
        self.assertEqual([['the', 'cat', 'there', 'here']],result['text'].tolist())