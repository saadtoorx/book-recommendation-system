#Importing necessary libraries
import pandas as pd
import gradio as gr
from sklearn.metrics.pairwise import cosine_similarity

#Loading Dataset
data = pd.read_csv('books_rating.csv')
data.head() 

#Creating user book matrix
user_book_matrix = data.pivot_table(index='user_id', columns='book_title', values = 'rating').fillna(0)
user_book_matrix

#Calculating cosine similarity between users
user_similarity = cosine_similarity(user_book_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_book_matrix.index, columns=user_book_matrix.index)
user_similarity_df

# Function to recommend books based on user similarity
def recommend_books(user_id, top_n=3):
    if user_id not in user_similarity_df.index:
        return ["User not found in the dataset."]

    similar_users = user_similarity_df[user_id].sort_values(ascending=False).drop(user_id)

    recommended_books = {}
    for sim_user, similarity in similar_users.items():
        rated_books = user_book_matrix.loc[sim_user]
        for book, rating in rated_books[rated_books > 0].items():
            if user_book_matrix.loc[user_id, book] == 0:
                recommended_books[book] = recommended_books.get(book, 0) + rating * similarity

    recommended_books = sorted(recommended_books.items(), key=lambda x: x[1], reverse=True)
    return [book for book, _ in recommended_books[:top_n]]

#Gradio interface & User Input
demo = gr.Interface(
    fn = recommend_books,
    inputs = [
        gr.Number(label="Enter User ID (1-100)", precision=0),
        gr.Number(label="Number of Books to Recommend", value=3, precision=0)

    ],
    outputs = gr.List(label="Recommended Books"),
    title = "Book Recommendation System",
    description = "Enter a user ID to get personalized book recommendations based on other users' ratings."
)

#Calling Function
demo.launch()