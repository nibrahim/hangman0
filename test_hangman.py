import hangman

def test_select_random_word_min_length():
    secret_word = hangman.get_random_word()
    assert len(secret_word) >= 6

def test_select_random_word_no_non_alpha_chars():
    secret_word = hangman.get_random_word()
    assert secret_word.isalpha()

def test_select_random_word_no_capitals():
    secret_word = hangman.get_random_word()
    assert secret_word.islower()










    
