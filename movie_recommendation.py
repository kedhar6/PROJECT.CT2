import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self):
        self.movies = pd.DataFrame({
            'title': ['Inception', 'Interstellar', 'The Dark Knight', 'Juno', 'Her'],
            'genres': ['Action|Sci-Fi|Thriller', 'Adventure|Drama|Sci-Fi', 
                      'Action|Crime|Drama', 'Comedy|Drama|Romance', 'Drama|Romance|Sci-Fi'],
            'rating': [8.8, 8.6, 9.0, 7.5, 8.0]
        })
        self.genre_matrix = self.movies['genres'].str.get_dummies(sep='|')

    def recommend_movies(self, user_preferences, n_recommendations=3):
        user_profile = pd.DataFrame([user_preferences])
        similarity_scores = cosine_similarity(
            user_profile[user_preferences.keys()],
            self.genre_matrix[user_preferences.keys()]
        )
        similar_movies = list(enumerate(similarity_scores[0]))
        sorted_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
        
        recommendations = []
        for i, score in sorted_movies[:n_recommendations]:
            recommendations.append({
                'title': self.movies.iloc[i]['title'],
                'genres': self.movies.iloc[i]['genres'],
                'rating': self.movies.iloc[i]['rating'],
                'similarity_score': score
            })
        
        return recommendations

if __name__ == "__main__":
    recommender = MovieRecommender()
    user_preferences = {
        'Action': 1.0,
        'Drama': 0.8,
        'Sci-Fi': 0.9,
        'Romance': 0.5
    }
    recommendations = recommender.recommend_movies(user_preferences)
    print("\nRecommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie['title']} ({movie['genres']}) - Rating: {movie['rating']:.1f}")
