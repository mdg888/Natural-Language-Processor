import re
import pandas as pd

def tokenise(data):
    data['text'] = data['text'].apply(lambda words: re.sub(r'[^A-Za-z0-9\s]', '', words))
    data['text'] = data['text'].fillna('').astype(str).str.split()
    return data