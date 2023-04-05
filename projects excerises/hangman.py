import random
easy_words = ['string', 'loop', 'python', 'print', 'run']
medium_words = ['module', 'input', 'logic', 'output']
hard_words = ['graphics window', 'variable', 'iteration', 'modules']
random_words = ['string', 'loop', 'python', 'print', 'run', 'graphics window',
                 'variable', 'iteration', 'modules', 'module', 'input', 'logic', 'output']


def get_valid_word(easy_words , medium_words, hard_words, random_words):
    word = random.choice(easy_words , medium_words , hard_words, random_words)



def play():
    user = input( f" We will play hangman. Choose from\n easy, mid, hard or random \n for different level. ")
    
    if user == "mid":
       random.choice