import requests
from openpyxl import Workbook
from datetime import datetime, timedelta

API_KEY = 'c74640ebfbd74f679440876cbc6fe76b'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

def get_movie_news(movie_title):
    today = datetime.now()
    one_month_ago = today - timedelta(days=30)
    
    params = {
        'q': f'"{movie_title}"',  
        'apiKey': API_KEY,
        'language': 'en',
        'region': 'us',  
        'from': one_month_ago.strftime('%Y-%m-%d'),
        'to': today.strftime('%Y-%m-%d'),
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    if 'articles' in data:
        return data['articles']
    else:
        print(f"No 'articles' key found in the response for {movie_title}")
        return []

movies = [
    "Oppenheimer",
    "Spider-Man: Across the Spider-Verse",
    "Mission: Impossible - Dead Reckoning Part One",
    "Past Lives",
    "Anatomy of a Fall",
    "The Holdovers",
    "About Dry Grasses",
    "Fallen Leaves",
    "The Zone of Interest",
    "Poor Things",
    "Dungeons & Dragons: Honor Among Thieves",
    "A Haunting in Venice",
    "Barbie",
    "Asteroid City",
    "Talk to Me",
    "The Color Purple",
    "Five Nights at Freddy's",
    "Indiana Jones and the Dial of Destiny",
    "Beau Is Afraid"
]
movies_additional = [
    "Blue Beetle",
    "Gran Turismo",
    "The Nun II",
]
workbook = Workbook()
sheet = workbook.active
sheet.append(['Movie', 'Article Date', 'Article Title', 'Article Description'])

for movie in movies_additional:
    news_articles = get_movie_news(movie)

    for article in news_articles:
        article_date = article.get('publishedAt', 'N/A')
        title = article.get('title', 'N/A')
        description = article.get('description', 'N/A')

        if description is not None and (f'{movie.lower()}' in title.lower() or f'{movie.lower()}' in description.lower()):
            sheet.append([movie, article_date, title, description])

workbook.save('movie_news_exact_title_match.xlsx')

