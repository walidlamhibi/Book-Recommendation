import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Télécharger les ressources nécessaires pour NLTK
nltk.download('stopwords')

def fetch_google_books(query, max_results=40):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def extract_book_details(books_data):
    books = []
    if 'items' in books_data:
        for item in books_data['items']:
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', 'Title not available')
            authors = volume_info.get('authors', ['Author not available'])
            description = volume_info.get('description', 'Description not available')
            categories = volume_info.get('categories', ['Genre not available'])
            books.append({
                'title': title,
                'authors': authors,
                'description': description,
                'categories': categories
            })
    return books

def preprocess_descriptions(books):
    descriptions = [book['description'] for book in books if 'description' in book]
    vectorizer = TfidfVectorizer(stop_words=nltk.corpus.stopwords.words('english'))
    tfidf_matrix = vectorizer.fit_transform(descriptions)
    return tfidf_matrix, vectorizer

def recommend_books(user_query, books, tfidf_matrix, vectorizer):
    user_query_tfidf = vectorizer.transform([user_query])
    cosine_similarities = cosine_similarity(user_query_tfidf, tfidf_matrix).flatten()
    top_indices = cosine_similarities.argsort()[-10:][::-1]
    recommended_books = [books[i] for i in top_indices]
    return recommended_books
