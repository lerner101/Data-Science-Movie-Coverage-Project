import csv
import matplotlib.pyplot as plt

def count_topics(csv_file):
    topic_dict = {}

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            topic = row['Annotation'].strip()

            words = topic.split()
            if len(words) > 3:
                topic = ' '.join(words[:3])

            if topic in topic_dict:
                topic_dict[topic] += 1
            else:
                topic_dict[topic] = 1

    return topic_dict

def plot_bar_graph(dictionary, output_filename):
    topics = list(dictionary.keys())
    counts = list(dictionary.values())

    plt.bar(topics, counts)
    plt.xlabel('Movies')
    plt.ylabel('Count')
    plt.title('Oppenheimer Topic Counts')
    plt.xticks(rotation=90)  
    plt.tight_layout() 


    plt.savefig(output_filename)

csv_file_path = 'topic.csv'
output_png_file = 'Oppenheimer_topic_counts.png'  
result = count_topics(csv_file_path)

print(result)

plot_bar_graph(result, output_png_file)
