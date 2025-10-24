import json

class SpamModel:
    
    def __init__(self, tokenizer, stopword_remover, lemmatizer, stemmer, nlp_engine):
        self.tokenizer = tokenizer
        self.stopword_remover = stopword_remover
        self.lemmatizer = lemmatizer
        self.stemmer = stemmer
        self.nlp_engine = nlp_engine

        # assist with the user choice
        self.preprocessing_type = None
        self.chosen = False

    def clean_data(self, data):
        """Step 1: Tokenize and remove stopwords"""
        tokens = self.tokenizer(data)
        clean_tokens = self.stopword_remover(tokens)
        return clean_tokens

    def apply_preprocessing(self):
        """Step 2: Ask user if they want lemmatization or stemming"""
        while True:
            choice = input("Select 1 for lemmantisation or 2 for stemming: ").strip()
            if choice in ["1","2"]:
                if int(choice) == 1:
                    self.preprocessing_type = True
                else:
                    self.preprocessing_type = False
                break
            else:
                print("please answer 1 or 2")
        self.chosen = True    

    def preprocessing(self, data):
        """Combine cleaning + preprocessing"""
        clean = self.clean_data(data)
        
        if not self.chosen:
            self.apply_preprocessing()

        if self.preprocessing_type: # true for lemmantisation
            processed = self.lemmatizer(clean)
            return processed
        
        processed = self.stemmer(clean)  # false for PortStem
        return processed

    def train_model(self, df, ngrams):
        """Train the model using text column and spam labels"""
        self.preprocessing(df)

        # Train NLP engine with tokens + labels
        self.nlp_engine(df, ngrams)


    def predict(self, data):
        """Predict if email is SPAM or HAM"""
        processed = self.preprocessing(data)
        # opens the dictionary
        with open("data/spam_dictionary.json", "r", encoding="utf-8") as file:
            dictionary = json.load(file)

        list_of_probs = []

        # goes through list of words to append them to the list
        for word in processed['text']:
            for w in word:
                w = w.strip()
                if not w:  # skip empty strings or spaces
                    continue
                try:
                    list_of_probs.append(dictionary[w]['p_spam'])
                except KeyError:
                    continue

        if len(list_of_probs) == 0:
            return "No Words Found!"
        # finds the mean of all probabilities
        prop_val_mean = sum(list_of_probs)* 1/len(list_of_probs)
        # returns classification
        return self.classify(prop_val_mean)

    def classify(self, probability):
        """Convert probability to SPAM or HAM"""
        return "SPAM" if probability > 0.5 else "HAM"
