"""Standalone NLTK vs spaCy benchmark."""

import time
import pandas as pd
from nltk_pipeline import preprocess as nltk_preprocess
from spacy_pipeline import preprocess as spacy_preprocess


def benchmark(texts, processor):
    start = time.perf_counter()
    for text in texts:
        processor(text)
    elapsed = time.perf_counter() - start
    return elapsed, len(texts) / elapsed


if __name__ == '__main__':
    df = pd.read_csv('Tweets.csv')
    texts = df['text'].dropna().astype(str).head(10000).tolist()

    rows = []

    for size in [1000, 5000, 10000]:
        sample = texts[:size]

        nt, ns = benchmark(sample, nltk_preprocess)
        st, ss = benchmark(sample, spacy_preprocess)

        rows.append({'Library': 'NLTK', 'Size': len(sample), 'Seconds': nt, 'Tweets_Per_Second': ns})
        rows.append({'Library': 'spaCy', 'Size': len(sample), 'Seconds': st, 'Tweets_Per_Second': ss})

    result = pd.DataFrame(rows)
    result.to_csv('standalone_benchmark_results.csv', index=False)
    print(result)