import nltk
import string
import random
from random import randint
import itertools
from contextualizer import webScapper
#STMT_MAXLEN = 20
NLTK_CONTEXT_TAGS = [
    'NN',
    'NNP',
    'JJ',
]

NLTK_PLURALS = [
    'NNS',
    'NNPS',
]

def singularize_plural_word(word):
    return nltk.pos_tag(word[:-1])[0]


def get_probable_contexts(statement):

    if type(statement) != str:
        raise ValueError("INVALID ARGUMENT: Expected a string")

    translator = str.maketrans('', '', string.punctuation)
    refined_stmt = statement.translate(translator)

    _tokens = nltk.word_tokenize(refined_stmt)

    #if len(_tokens) > STMT_MAXLEN:
     #   raise ValueError("INVALID STATEMEMT: more than {} words".format(STMT_MAXLEN))

    contexts = []

    for token, tag in nltk.pos_tag(_tokens):
        if tag in NLTK_PLURALS:
            token, tag = singularize_plural_word(token)

        if tag in NLTK_CONTEXT_TAGS:
            contexts.append(token.lower())

    def _get_combinations(contexts):
        ctx_set = set()
        for i, j in itertools.combinations(range(len(contexts)+1), 2):
            ctx_set.add(' '.join(contexts[i:j]))

        return ctx_set

    return contexts


def get_context_from_article(url):
    content = webScapper.return_web_content(url)
    contexts = get_probable_contexts(content)

    b = set()
    unique_context = []

    for x in contexts:
        if x not in b and len(x) >= 3:
            unique_context.append(x)
            b.add(x)

    num = randint(5, 6)
    random_contexts = random.sample(unique_context, num)
    return random_contexts

