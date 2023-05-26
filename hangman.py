import random


def get_random_word():
    candidate_words = []
    with open("/usr/share/dict/words") as f:
        for word in f:
            word = word.strip()
            if len(word) >= 6 and word.islower() and word.isalpha():
                candidate_words.append(word)
    word = random.choice(candidate_words)
    return word
