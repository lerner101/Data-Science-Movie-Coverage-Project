import json
import math
import argparse
import os
import pandas as pd
from collections import defaultdict
import string

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return ' '.join([word for word in text.split() if word.isalpha()])

def load_stopwords(stopwords_file):
    with open(stopwords_file, 'r') as file:
        stop_words = set(file.read().splitlines())
    return stop_words

def compute_tfidf(tf, idf):
    return tf * idf

def compute_movie_lang(movie_counts_file, num_words):
    with open(movie_counts_file) as f:
        movie_counts = json.load(f)

    total_movies = len(movie_counts)
    movie_language = {}

    for movie_name, word_counts in movie_counts.items():
        tfidf_scores = []
        for word, tf in word_counts.items():
            num_movies_with_word = sum(1 for counts in movie_counts.values() if word in counts)
            idf = math.log(total_movies / num_movies_with_word)
            tfidf = compute_tfidf(tf, idf)
            tfidf_scores.append((word, tfidf))

        tfidf_scores.sort(key=lambda x: x[1], reverse=True)
        movie_language[movie_name] = [word for word, _ in tfidf_scores[:num_words]]

    output_path = os.path.join(os.path.dirname(movie_counts_file), 'Distinctive_movie_words.json')
    with open(output_path, 'w') as f:
        json.dump(movie_language, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description='Compute distinctive movie words based on TF-IDF scores.')
    parser.add_argument('-c', '--movie_counts_file', required=True, help='Path to the JSON file containing word counts for each movie.')
    parser.add_argument('-n', '--num_words', type=int, required=True, help='Number of distinctive words to consider for each movie.')

    args = parser.parse_args()
    compute_movie_lang(args.movie_counts_file, args.num_words)

if __name__ == "__main__":
    main()
