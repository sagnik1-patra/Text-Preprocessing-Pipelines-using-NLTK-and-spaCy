"""spaCy preprocessing pipeline."""

import spacy
from preprocessing_library import clean_text

nlp = spacy.load('en_core_web_sm')

NEGATIONS = {'not', 'no', 'nor', 'never'}


def preprocess(text):

    cleaned = clean_text(text)
    doc = nlp(cleaned)

    tokens = []
    lemmas = []
    pos_tags = []
    entities = []

    for token in doc:
        if token.is_space or token.is_punct or not token.is_alpha:
            continue

        tokens.append(token.text.lower())
        pos_tags.append((token.text, token.pos_))

        if not token.is_stop or token.text.lower() in NEGATIONS:
            lemmas.append(token.lemma_.lower())

    for ent in doc.ents:
        entities.append({'text': ent.text, 'label': ent.label_})

    return {
        'tokens': tokens,
        'lemmas': lemmas,
        'pos': pos_tags,
        'entities': entities
    }