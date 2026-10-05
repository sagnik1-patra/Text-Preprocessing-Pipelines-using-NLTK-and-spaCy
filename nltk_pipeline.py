"""NLTK preprocessing pipeline."""

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import pos_tag
from preprocessing_library import clean_text

NEGATIONS = {'not', 'no', 'nor', 'never'}
CUSTOM = {'amp', 'rt', 'via', 'tweet', 'tweets'}

STOPWORDS = set(stopwords.words('english'))
STOPWORDS -= NEGATIONS
STOPWORDS.update(CUSTOM)

porter = PorterStemmer()
snowball = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()


def wn_pos(tag):
    if tag.startswith('J'): return wordnet.ADJ
    if tag.startswith('V'): return wordnet.VERB
    if tag.startswith('N'): return wordnet.NOUN
    if tag.startswith('R'): return wordnet.ADV
    return wordnet.NOUN


def preprocess(text):
    text = clean_text(text)
    tokens = [x for x in word_tokenize(text) if x.isalpha()]
    filtered = [x for x in tokens if x not in STOPWORDS or x in NEGATIONS]
    tagged = pos_tag(filtered) if filtered else []
    lemmas = [lemmatizer.lemmatize(x, wn_pos(tag)) for x, tag in tagged]

    return {
        'tokens': tokens,
        'filtered': filtered,
        'porter': [porter.stem(x) for x in filtered],
        'snowball': [snowball.stem(x) for x in filtered],
        'lemmas': lemmas,
        'pos': tagged
    }