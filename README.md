# 🎬 Movie Recommendation System

This is a simple **content-based movie recommendation system** implemented in Python using pandas and scikit-learn. It uses cosine similarity to recommend movies based on user genre preferences.

## 📁 File Structure

- `movie_recommendation.py`: Main script containing the recommendation system logic.

## 🧠 How It Works

1. A small dataset of movies with genres and ratings is hardcoded.
2. The genre information is converted into a binary matrix using one-hot encoding.
3. A user profile (dictionary of genre preferences) is used to compute cosine similarity with all movies.
4. The top N most similar movies are recommended.

## 🚀 Getting Started

### 📦 Requirements

Make sure you have Python installed with the following packages:

```bash
pip install pandas scikit-learn
```

### ▶️ Running the Script

```bash
python movie_recommendation.py
```

The script will print out the top 3 recommended movies based on the default user preferences:

```python
user_preferences = {
    'Action': 1.0,
    'Drama': 0.8,
    'Sci-Fi': 0.9,
    'Romance': 0.5
}
```

### 🧾 Sample Output

```
Recommended Movies:
1. Inception (Action|Sci-Fi|Thriller) - Rating: 8.8
2. Interstellar (Adventure|Drama|Sci-Fi) - Rating: 8.6
3. The Dark Knight (Action|Crime|Drama) - Rating: 9.0
```

## 🛠 Customization

You can change the `user_preferences` dictionary to reflect different genre preferences.

You can also expand the hardcoded movie dataset in the constructor of the `MovieRecommender` class.

## 📌 Notes

- This is a basic prototype using a small static dataset.
- Cosine similarity is used for computing closeness between user preference and genre vectors.

## 📄 License

This project is provided for educational/demo purposes. You may use and modify it freely.