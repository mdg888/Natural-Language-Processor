def lemmantisation(data):

    if not data['text'].astype(bool).any():
        return []

    data['text'] = data['text'].apply(lambda words: [lemmantise(w) for w in words])
    return data

def lemmantise(word):
    word = word.lower()
    
    # Irregular verbs
    irregular_verbs = {
        'was': 'be', 'were': 'be', 'been': 'be', 'being': 'be', 'am': 'be', 'are': 'be', 'is': 'be',
        'had': 'have', 'has': 'have', 'having': 'have',
        'did': 'do', 'does': 'do', 'doing': 'do', 'done': 'do',
        'went': 'go', 'gone': 'go', 'going': 'go', 'goes': 'go',
        'said': 'say', 'says': 'say', 'saying': 'say',
        'made': 'make', 'makes': 'make', 'making': 'make',
        'took': 'take', 'takes': 'take', 'taken': 'take', 'taking': 'take',
        'came': 'come', 'comes': 'come', 'coming': 'come',
        'saw': 'see', 'seen': 'see', 'sees': 'see', 'seeing': 'see',
        'got': 'get', 'gets': 'get', 'gotten': 'get', 'getting': 'get',
        'gave': 'give', 'given': 'give', 'gives': 'give', 'giving': 'give',
        'found': 'find', 'finds': 'find', 'finding': 'find',
        'told': 'tell', 'tells': 'tell', 'telling': 'tell',
        'became': 'become', 'becomes': 'become', 'becoming': 'become',
        'left': 'leave', 'leaves': 'leave', 'leaving': 'leave',
        'felt': 'feel', 'feels': 'feel', 'feeling': 'feel',
        'brought': 'bring', 'brings': 'bring', 'bringing': 'bring',
        'began': 'begin', 'begun': 'begin', 'begins': 'begin', 'beginning': 'begin',
        'kept': 'keep', 'keeps': 'keep', 'keeping': 'keep',
        'held': 'hold', 'holds': 'hold', 'holding': 'hold',
        'wrote': 'write', 'written': 'write', 'writes': 'write', 'writing': 'write',
        'stood': 'stand', 'stands': 'stand', 'standing': 'stand',
        'ran': 'run', 'runs': 'run', 'running': 'run',
        'bought': 'buy', 'buys': 'buy', 'buying': 'buy',
        'spoke': 'speak', 'spoken': 'speak', 'speaks': 'speak', 'speaking': 'speak', 
        'better': 'good'
    }
    
    if word in irregular_verbs:
        return irregular_verbs[word]
    
    # Irregular plurals
    irregular_plurals = {
        'children': 'child', 'men': 'man', 'women': 'woman', 'people': 'person',
        'feet': 'foot', 'teeth': 'tooth', 'geese': 'goose', 'mice': 'mouse',
        'oxen': 'ox', 'sheep': 'sheep', 'deer': 'deer', 'fish': 'fish',
        'lives': 'life', 'wives': 'wife', 'knives': 'knife', 'leaves': 'leaf',
    }
    
    if word in irregular_plurals:
        return irregular_plurals[word]
    
    if word.endswith('ing'):
        if len(word) > 5 and word[-4] == word[-5]:
            return word[:-4]
        return word[:-3]
    
    if word.endswith('ed'):
        if len(word) > 4 and word[-3] == word[-4]:
            return word[:-3]
        return word[:-2]
    
    if word.endswith('ies') and len(word) > 4:
        return word[:-3] + 'y'
    
    if word.endswith('es') and len(word) > 3:
        if word[-3] in 'sxz' or word[-4:-2] in ['ch', 'sh']:
            return word[:-2]
    
    if word.endswith('s') and len(word) > 2:
        return word[:-1]
    
    if word.endswith('ly') and len(word) > 4:
        return word[:-2]
    
    if word.endswith('er') and len(word) > 4:
        if word[-3] == word[-4]:
            return word[:-3]
        return word[:-2]
    
    if word.endswith('est') and len(word) > 5:
        if word[-4] == word[-5]:
            return word[:-4]
        return word[:-3]
    
    return word
