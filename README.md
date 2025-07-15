
# 🔍 Book Recommendation System using Cosine Similarity

Get personalized book recommendations 📚 based on what similar users liked!  
This simple machine learning project uses user-based collaborative filtering and cosine similarity to recommend top-rated books.

---

## 🧠 About the Project

This project creates a book recommendation system using a dataset of user ratings. It builds a user-book matrix and calculates **cosine similarity** between users. When a user ID is entered, the system suggests books that similar users have rated highly — but the target user hasn’t read yet.

The project also includes a **Gradio web interface** to make the recommendations interactive and easy to use.

---

## 🚀 Features

- 📊 Build user-book matrix from raw rating data  
- 🔗 Compute user-user similarity using cosine similarity  
- 📚 Recommend unread books based on similar users' preferences  
- 💡 Easy-to-use interface using Gradio  
- 🧠 Adjustable number of recommendations

---

## 🛠️ Tech Stack

- Python 3.x  
- pandas  
- scikit-learn  
- gradio  

---

## 📁 Project Structure

```
book-recommendation-system/
├── app.py                     # Main Gradio app file (this one runs)
├── app.ipynb             # Jupyter notebook version
├── books_rating.csv           # Ratings dataset
├── images/
│   ├── output1.png            # Example output screenshot
│   ├── output2.png
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation

```

---

## 💻 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/saadtoorx/book-recommendation-system.git
cd book-recommendation-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python main.py
```

### 4. Try It Out

- Enter a User ID (1–100)
- Choose how many book recommendations you want
- View personalized book suggestions!

---

## 📷 Sample Output

- 🟢 Recommended book list for input user
- 🧮 Based on cosine similarity with other users

---

## 🧾 License

This project is licensed under the **MIT License**.

---

## 👤 Author

Made with 💡 by [@saadtoorx](https://github.com/saadtoorx)  
If you found this helpful, ⭐ star the repo and feel free to fork!
