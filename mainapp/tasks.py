from celery import shared_task
import feedparser
import pandas as pd
import re
import mysql.connector


# Clean text
# def clean_text(text):
#     text = re.sub(r'[^\w\s]', '', text)
#     return text.lower()
#
#
# # Function to categorize articles
# def categorize_article(text):
#     category_keywords = {
#         "Terrorism": ["terrorist", "attack", "bombing", "militants", "ISIS", "Al-Qaeda"],
#         "Protest/Political Unrest/Riot": ["protest", "demonstration", "riot", "unrest", "violence"],
#         'Positive/Uplifting/Development': ['uplifting', 'positive', 'celebrates', 'success', 'achievement', 'aid',
#                                            'help', 'support', 'development', 'progress', 'inauguration'],
#         'Natural Disasters': ['earthquake', 'flood', 'hurricane', 'cyclone', 'tsunami', 'disaster', 'natural disaster',
#                               'wildfire', 'drought', 'landslide', 'avalanche'],
#         'International Relations/Diplomacy': ['diplomacy', 'un', 'relations', 'treaty', 'trade agreement', 'alliance',
#                                               'sanctions', 'embassy', 'ambassador', 'talks'],
#         'War/Conflicts/Military': ['war', 'conflict', 'military', 'army', 'soldier', 'airstrike', 'battle', 'invasion',
#                                    'bombing', 'nato', 'defense']
#     }
#
#     text = clean_text(text)
#     for category, keywords in category_keywords.items():
#         if any(keyword in text for keyword in keywords):
#             return category
#     return "Others"
#
# @shared_task(bind=True)
# def parse_and_save_rss():
#     url = ["https://feeds.feedburner.com/NewshourWorld",
#            "http://rss.cnn.com/rss/cnn_topstories.rss",
#            "https://moxie.foxnews.com/google-publisher/politics.xml",
#            "https://qz.com/rss",
#            "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"]
#
#     articles = []
#     for i in url:
#         feed = feedparser.parse(i)
#         for entry in feed['entries']:
#             content_encoded = entry.get('content', 'No content available')
#             if isinstance(content_encoded, list) and len(content_encoded) > 0:
#                 content_encoded = content_encoded[0].get('value', 'No content available')
#             else:
#                 content_encoded = entry.get('summary_detail', {}).get('value', 'No content available')
#
#             article = {
#                 'title': entry.get('title'),
#                 'description': entry.get('description', 'No description available'),
#                 'content': content_encoded,
#                 'comments': entry.get('comments', 'No comments available'),
#                 'publication_date': entry.get('published', 'No date available'),
#                 'source_url': entry.get('link')
#             }
#             articles.append(article)
#
#     df = pd.DataFrame(articles)
#
#     # Combine title, description, and content into one column
#     df['combined_text'] = df['title'] + ' ' + df['description'] + ' ' + df['content']
#
#     # Categorize each article
#     df['category'] = df['combined_text'].apply(categorize_article)
#
#     df.drop(columns=['combined_text'], inplace=True)
#
#     # Save to MySQL
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='1234',
#             database='rss'
#         )
#
#         cursor = connection.cursor()
#
#         cursor.execute('''CREATE TABLE IF NOT EXISTS news_articles (
#                             id INT AUTO_INCREMENT PRIMARY KEY,
#                             title TEXT,
#                             description TEXT,
#                             content TEXT,
#                             comments TEXT,
#                             publication_date TEXT,
#                             source_url TEXT,
#                             category VARCHAR(255)
#                         )''')
#
#         for index, row in df.iterrows():
#             cursor.execute('''INSERT INTO news_articles (title, description, content, comments, publication_date, source_url, category)
#                               VALUES (%s, %s, %s, %s, %s, %s, %s)''',
#                            (row['title'], row['description'], row['content'], row['comments'], row['publication_date'],
#                             row['source_url'], row['category']))
#
#         connection.commit()
#
#     except mysql.connector.Error as error:
#         print(f"Error: {error}")
#
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")
#     return print("Doe")

def rand():
    print("nmaaana")
    return print("done")