import os
import pandas as pd
from collections import defaultdict
import string
import json
import argparse

def preprocess_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return ' '.join([word for word in text.split() if word.isalpha()])
    else:
        return '' 

def load_stopwords(stopwords_file):
    with open(stopwords_file, 'r') as file:
        stop_words = set(file.read().splitlines())
    return stop_words

def compile_word_counts(excel_file, output_file, stopwords_file):
    word_counts = defaultdict(lambda: defaultdict(int))

    df = pd.read_csv(excel_file)
    stop_words = load_stopwords(stopwords_file)

    for index, row in df.iterrows():
        topic = row['Topics']
        if pd.notna(topic):
            topic = topic.lower()

            if topic in ['production', 'actor/director', 'story telling', 'release and promotion', 'economic aspects', 'comparison', 'review']:
                title = preprocess_text(row['Article Title'])
                description = preprocess_text(row['Article Description'])
                
                title_words = title.split()
                description_words = description.split()

                for word in title_words + description_words:
                    if word not in stop_words:
                        word_counts[topic][word] += 1


    with open(output_file, 'w') as f:
        json.dump(word_counts, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description='Compile word counts for specified movies from Excel data.')
    parser.add_argument('-o', '--output_file', required=True, help='Path to the output JSON file for word counts.')
    parser.add_argument('-e', '--excel_file', required=True, help='Path to the Excel or CSV file containing movie data.')
    parser.add_argument('-s', '--stopwords_file', required=True, help='Path to the file containing stopwords.')

    args = parser.parse_args()
    compile_word_counts(args.excel_file, args.output_file, args.stopwords_file)

if __name__ == "__main__":
    main()
