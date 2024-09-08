import tkinter as tk
from tkinter import messagebox, Scrollbar, Listbox, END
from book_processing import fetch_google_books, extract_book_details, preprocess_descriptions, recommend_books
from recommender import generate_recommendations

# Variables pour stocker les résultats de recherche
search_results = []

def search_books(entry_query, listbox_books, button_recommend):
    query = entry_query.get()
    if not query:
        messagebox.showwarning("Attention", "Veuillez entrer une requête.")
        return
    
    books_data = fetch_google_books(query)
    
    if books_data:
        books = extract_book_details(books_data)
        tfidf_matrix, vectorizer = preprocess_descriptions(books)
        recommended_books = recommend_books(query, books, tfidf_matrix, vectorizer)
        
        # Stocker les résultats de la recherche
        search_results.append({
            'query': query,
            'books': books,
            'tfidf_matrix': tfidf_matrix,
            'vectorizer': vectorizer
        })
        
        # Efface la liste précédente
        listbox_books.delete(0, END)
        
        # Affiche les résultats dans la liste
        for idx, book in enumerate(recommended_books, 1):
            listbox_books.insert(END, f"{idx}. Titre: {book['title']}\n   Auteurs: {', '.join(book['authors'])}\n   Description: {book['description']}\n")
        
        # Affiche le bouton de recommandation si trois recherches sont effectuées
        if len(search_results) == 3:
            button_recommend.pack(pady=10)
    else:
        messagebox.showerror("Erreur", "Impossible de récupérer les informations des livres depuis Google Books. Veuillez réessayer plus tard.")

def setup_ui(root):
    # Cadre pour l'entrée de la requête
    frame_query = tk.Frame(root)
    frame_query.pack(pady=20)

    label_query = tk.Label(frame_query, text="Entrez votre requête :")
    label_query.pack(side=tk.LEFT)

    entry_query = tk.Entry(frame_query, width=50)
    entry_query.pack(side=tk.LEFT, padx=10)

    # Bouton de recherche
    button_search = tk.Button(root, text="Rechercher", command=lambda: search_books(entry_query, listbox_books, button_recommend))
    button_search.pack()

    # Liste des résultats
    frame_results = tk.Frame(root)
    frame_results.pack(pady=20)

    scrollbar = Scrollbar(frame_results)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_books = Listbox(frame_results, width=100, yscrollcommand=scrollbar.set)
    listbox_books.pack()

    scrollbar.config(command=listbox_books.yview)

    # Bouton de recommandation
    button_recommend = tk.Button(root, text="Générer des Recommandations", command=lambda: generate_recommendations(search_results, listbox_books))
