# Building and Benchmarking Text Preprocessing Pipelines using NLTK and spaCy

## Overview

This project develops and benchmarks text preprocessing pipelines using NLTK and spaCy on noisy Twitter text.

The implementation uses a 10,000 tweet subset of the Twitter US Airline Sentiment dataset.

## Features

- Lowercase conversion
- URL removal
- Mention removal
- Hashtag processing
- Number removal
- Punctuation removal
- Emoji removal and emoji-to-text conversion
- Contraction expansion
- Repeated-character normalization
- Stopword removal
- Negation preservation
- NLTK tokenization
- Porter stemming
- Snowball stemming
- WordNet lemmatization
- NLTK POS tagging
- spaCy tokenization
- spaCy lemmatization
- spaCy POS tagging
- Named Entity Recognition
- Dependency parsing
- Custom spaCy EntityRuler
- Performance benchmarking
- Memory benchmarking
- Vocabulary analysis

## Main Source Files

- `preprocessing_library.py`
- `nltk_pipeline.py`
- `spacy_pipeline.py`
- `benchmark.py`

## Benchmarking

The pipelines are benchmarked using 1,000, 5,000 and 10,000 tweets.

Metrics include:

- Processing time
- Tweets per second
- Peak memory
- Average tokens
- Vocabulary size

## Quality Evaluation

`quality_review_100_samples.csv` provides 100 examples for manual evaluation of lemmatization, POS tagging and NER.

The original dataset does not contain gold-standard lemma, POS or NER labels, so the project does not fabricate accuracy percentages.

## Installation

Install dependencies using:

`pip install -r requirements.txt`

Then install the spaCy English model:

`python -m spacy download en_core_web_sm`

## Submission

The submission ZIP intentionally excludes the original dataset, processed 10,000-row datasets, virtual environments, caches, installed language models and redundant generated files.

Only source code, reports, benchmark summaries, the 100-sample quality file and representative result visualizations are included.