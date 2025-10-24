from collections import Counter
import json

def nlp(data,alpha):
    # setting params 
    min_count = 5
    ngram = 1

    count_spam = Counter()
    count_ham = Counter()
    msg_count_spam = 0
    msg_count_ham = 0 

    # processing the data
    for index, cols in data.iterrows():
        tokens = cols['text']
        if ngram > 1:
            tokens = make_ngrams(tokens,ngram)
    
        if cols['spam'] == "1":
            msg_count_spam += 1
            count_spam.update(tokens)
        else:
            msg_count_ham += 1
            count_ham.update(tokens)
        
    # calculate totals and prior proabilities
    total_tokens_spam = sum(count_spam.values())
    total_tokens_ham = sum(count_ham.values())

    vocab = set(count_spam.keys()) | set(count_spam.keys())
    V = len(vocab)

    P_spam_prior = msg_count_spam / (msg_count_spam + msg_count_ham)

    # building the dictionary
    dictionary = {}
    for w in vocab:
        Cs = count_spam[w]
        Ch = count_ham[w]

        p_w_given_spam = (Cs + alpha) / (total_tokens_spam + alpha * V)
        p_w_given_ham = (Ch + alpha) / (total_tokens_ham + alpha * V)

        p_spam_given_w = (p_w_given_spam * P_spam_prior) / \
                     (p_w_given_spam * P_spam_prior + p_w_given_ham * (1 - P_spam_prior))
        

        total_count = Cs + Ch
        if total_count >= min_count:
            dictionary[w] = {
                "count_spam": Cs,
                "count_ham": Ch,
                "p_spam": round(p_spam_given_w, 6)
            }
    
    # Step 4: Export
    with open("data/spam_dictionary.json", "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)
    

def make_ngrams(tokens, n=1):
    if n == 1:
        return tokens
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngram = '_'.join(tokens[i:i+n])
        ngrams.append(ngram)
    return ngrams
