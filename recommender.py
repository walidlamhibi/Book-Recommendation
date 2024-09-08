from collections import Counter
from tkinter import END, messagebox
from book_processing import fetch_google_books, extract_book_details

def generate_recommendations(search_results, listbox_books):
    if len(search_results) < 3:
        messagebox.showwarning("Attention", "Veuillez effectuer les trois recherches avant de générer des recommandations.")
        return
    
    all_books = []
    all_genres = []
    all_authors = []
    
    for result in search_results:
        all_books.extend(result['books'])
        all_genres.extend([genre for book in result['books'] for genre in book['categories']])
        all_authors.extend([author for book in result['books'] for author in book['authors']])
    
    # Trouver les genres et auteurs dominants
    genre_counts = Counter(all_genres)
    dominant_genres = [genre for genre, count in genre_counts.items() if count > 1]
    
    author_counts = Counter(all_authors)
    dominant_authors = [author for author, count in author_counts.items() if count > 1]
    
    # Rechercher des livres par genres dominants et auteurs dominants
    recommendations = []
    
    for author in dominant_authors:
        author_books_data = fetch_google_books(f'inauthor:{author}')
        if author_books_data:
            author_books = extract_book_details(author_books_data)
            recommendations.extend(author_books)
    
    for genre in dominant_genres:
        genre_books_data = fetch_google_books(f'subject:{genre}')
        if genre_books_data:
            genre_books = extract_book_details(genre_books_data)
            recommendations.extend(genre_books)
    
    # Limiter à 10 recommandations uniques
    unique_recommendations = []
    seen_titles = set()
    for book in recommendations:
        if book['title'] not in seen_titles:
            seen_titles.add(book['title'])
            unique_recommendations.append(book)
        if len(unique_recommendations) == 10:
            break
    
    # Efface la liste précédente
    listbox_books.delete(0, END)
    
    # Affiche les résultats de recommandation dans la liste
    for idx, book in enumerate(unique_recommendations, 1):
        listbox_books.insert(END, f"{idx}. Titre: {book['title']}\n   Auteurs: {', '.join(book['authors'])}\n   Description: {book['description']}\n")
