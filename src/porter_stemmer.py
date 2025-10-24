def PoterStem(word):

    # Step 1a: Handle plurals
    if word.endswith("sses"):
        word = word[:-4] + "ss"
    elif word.endswith("ies"):
        word = word[:-3] + "i"
    elif word.endswith("s") and not word.endswith("ss"):
        word = word[:-1]
    
    # Step 1b: Handle past tense
    if word.endswith("eed"):
        if measure(word[:-3]) > 0:
            word = word[:-3] + "ee"
    elif word.endswith("ed"):
        stem = word[:-2]
        if has_vowel(stem):
            word = stem
            # Apply additional rules
            if word.endswith("at") or word.endswith("bl") or word.endswith("iz"):
                word = word + "e"
            elif word[-2:] in ["ll", "ss", "zz"] and measure(word) > 1:
                word = word[:-1]
            elif measure(word) == 1 and cvc(word):
                word = word + "e"
    elif word.endswith("ing"):
        stem = word[:-3]  # Fixed: 'ing' is 3 characters
        if has_vowel(stem):
            word = stem
            # Apply additional rules
            if word.endswith("at") or word.endswith("bl") or word.endswith("iz"):
                word = word + "e"
            elif word[-2:] in ["ll", "ss", "zz"] and measure(word) > 1:
                word = word[:-1]
            elif measure(word) == 1 and cvc(word):
                word = word + "e"
    
    # Step 1c: Handle 'y'
    if word.endswith("y") and has_vowel(word[:-1]):
        word = word[:-1] + "i"
    
    # Step 2: Replace suffixes
    step2_dict = {
        "ational": "ate",
        "tional": "tion",
        "enci": "ence",
        "anci": "ance",
        "izer": "ize",
        "bli": "ble",
        "alli": "al",
        "entli": "ent",
        "eli": "e",
        "ousli": "ous",
        "ization": "ize",
        "ation": "ate",
        "ator": "ate",
        "alism": "al",
        "iveness": "ive",
        "fulness": "ful",
        "ousness": "ous",
        "aliti": "al",
        "iviti": "ive",
        "biliti": "ble",
        "logi": "log"
    }

    for suffix in step2_dict.keys():
        if word.endswith(suffix) and measure(word[:-len(suffix)]) > 0:
            word = word[:-len(suffix)] + step2_dict[suffix]
            break
    
    # Step 3: Replace suffixes
    step3_dict = {
        "icate": "ic",
        "ative": "",
        "alize": "al",
        "iciti": "ic",
        "ical": "ic",
        "ful": "",
        "ness": "",
        "iest": "i"
    }

    for suffix in step3_dict.keys():
        if word.endswith(suffix) and measure(word[:-len(suffix)]) > 0:
            word = word[:-len(suffix)] + step3_dict[suffix]
            break

    # Step 4: Remove suffixes
    step4_dict = {
        "al": "", "ance": "", "ence": "", "er": "", "ic": "",
        "able": "", "ible": "", "ant": "", "ement": "",
        "ment": "", "ent": "", "ou": "", "ism": "",
        "ate": "", "iti": "", "ous": "", "ive": "", "ize": ""
    }

    for suffix in step4_dict.keys():
        if word.endswith(suffix) and measure(word[:-len(suffix)]) > 1:
            word = word[:-len(suffix)]
            break
    
    # Special case for 'ion'
    if word.endswith("ion") and len(word) > 3:
        if measure(word[:-3]) > 1 and word[-4] in "st":
            word = word[:-3]
    
    # Step 5a: Remove 'e'
    if word.endswith("e"):
        stem = word[:-1]
        if measure(stem) > 1:
            word = stem
        elif measure(stem) == 1 and not cvc(stem):
            word = stem
    
    # Step 5b: Remove double 'l'
    if word.endswith("ll") and measure(word) > 1:
        word = word[:-1]

    return word


def measure(word):
    """Calculate the measure of a word (number of VC sequences)"""
    vowels = "aeiou"
    m = 0
    in_vowel_seq = False

    for char in word:
        if char in vowels:
            in_vowel_seq = True
        else:
            if in_vowel_seq:
                m += 1
                in_vowel_seq = False
    return m


def has_vowel(word):
    """Check if word contains a vowel"""
    vowel = ["a", "e", "i", "o", "u"]
    for char in word:
        if char in vowel:
            return True
    return False


def cvc(word):
    """
    Returns True if the word ends with a consonant-vowel-consonant sequence,
    where the last consonant is NOT w, x, or y.
    """
    if len(word) < 3:
        return False

    vowels = "aeiou"
    last_three = word[-3:]

    first, second, last = last_three[0], last_three[1], last_three[2]

    if (first not in vowels) and (second in vowels) and (last not in vowels) and last not in "wxy":
        return True
    return False

def run_porter(data):
    
    if not data['text'].astype(bool).any():
        return []

    data['text'] = data['text'].apply(lambda words: [PoterStem(w) for w in words])
    return data