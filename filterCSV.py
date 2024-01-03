import pandas as pd

def filter_excel(input_file, output_file):
    df = pd.read_excel(input_file)

    movie_related_words = [
        "Film",
        "Movie",
        "Cinema",
        "Actor",
        "Director",
        "Story",
        "Plot",
        "Scene",
        "Review",
        "Genre",
        "Performance",
        "Character",
        "Audience",
        "Cinematography",
        "Screenplay",
        "Release",
        "Box Office",
        "Award",
        "Entertainment",
        "Hollywood"
    ]

    filtered_df = df[df.apply(lambda row: any(word.lower() in str(row['Article Title']).lower() or word.lower() in str(row['Article Description']).lower() for word in movie_related_words), axis=1)]

    filtered_df.to_excel(output_file, index=False)

input_excel_file = 'movie_news.xlsx'
output_excel_file = 'movie_output.xlsx'
filter_excel("movie_news_exact_title_match.xlsx", "output_excel_file.xlsx")
