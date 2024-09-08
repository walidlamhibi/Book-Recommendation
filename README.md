# Book Recommendation System

This project is a book recommendation system based on user input and data fetched from the Google Books API. The system provides recommendations based on the content of books, including genres and authors, by analyzing multiple search results.

## Features

- **Book Search**: Users can search for books using keywords, and relevant results are fetched from the Google Books API.
- **Book Recommendations**: After conducting three searches, the system analyzes the genres and authors of the search results to generate personalized book recommendations.
- **Simple User Interface**: A minimalistic interface to provide a smooth user experience.
- **Error Handling**: Includes error messages for failed API requests and warnings for empty search queries.

## Technologies Used

- **Python**: Core language used for development.
- **Tkinter**: For building the graphical user interface.
- **Google Books API**: Used to fetch book data.
- **Requests**: For making HTTP requests to the API.
- **NLTK**: Used for natural language processing, specifically to handle stop words in book descriptions.
- **Scikit-learn**: Utilized for TF-IDF vectorization and cosine similarity calculations to recommend books.

## System Architecture

- **UI**: Built using Tkinter to handle user input and display results.
- **Book Processing**: Includes data fetching from the Google Books API, description preprocessing, and vectorization using TF-IDF.
- **Recommendation Engine**: Utilizes cosine similarity to compare book descriptions and generate recommendations based on dominant genres and authors.


## How It Works

### Search
Enter a keyword in the search bar to find books related to the topic.

### Recommendations
After three searches, the system will recommend books based on the most common genres and authors in the previous searches.

### Error Handling
The system will notify the user in case of:
- Connection issues
- Invalid input
