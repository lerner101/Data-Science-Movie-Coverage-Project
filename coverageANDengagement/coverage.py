import csv
import matplotlib.pyplot as plt

def count_movies(csv_file):
    movie_dict = {}

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            movie_name = row['Movie'].strip()

            words = movie_name.split()
            if len(words) > 3:
                movie_name = ' '.join(words[:3])

            if movie_name in movie_dict:
                movie_dict[movie_name] += 1
            else:
                movie_dict[movie_name] = 1

    return movie_dict

def plot_bar_graph(dictionary, output_filename):
    movie_names = list(dictionary.keys())
    counts = list(dictionary.values())

    plt.bar(movie_names, counts)
    plt.xlabel('Movies')
    plt.ylabel('Count')
    plt.title('Movie Counts')
    plt.xticks(rotation=90)  
    plt.tight_layout()  

    plt.savefig(output_filename)

csv_file_path = 'coverage.csv'
output_png_file = 'movie_counts.png'  
result = count_movies(csv_file_path)

print(result)

plot_bar_graph(result, output_png_file)
