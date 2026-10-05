"""Reusable social-media preprocessing functions."""

import re
import pandas as pd

try:
    import emoji
except ImportError:
    emoji = None

try:
    import contractions
except ImportError:
    contractions = None

URL_PATTERN = r"https?://\S+|www\.\S+"
MENTION_PATTERN = r"@\w+"
HASHTAG_PATTERN = r"#\w+"


def clean_text(text, keep_hashtags=True, keep_numbers=False, emoji_mode='text'):

    if pd.isna(text):
        return ''

    text = str(text).lower()

    if emoji is not None:
        if emoji_mode == 'remove':
            text = emoji.replace_emoji(text, replace='')
        elif emoji_mode == 'text':
            text = emoji.demojize(text, delimiters=(' ', ' '))

    if contractions is not None:
        text = contractions.fix(text)

    text = re.sub(URL_PATTERN, ' ', text)
    text = re.sub(MENTION_PATTERN, ' ', text)

    if keep_hashtags:
        text = re.sub(r'#(\w+)', r'\1', text)
    else:
        text = re.sub(HASHTAG_PATTERN, ' ', text)

    text = re.sub(r'(.)\1{2,}', r'\1\1', text)

    if not keep_numbers:
        text = re.sub(r'\b\d+(?:\.\d+)?\b', ' ', text)

    text = text.replace('_', ' ')
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text