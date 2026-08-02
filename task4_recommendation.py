"""
CODSOFT - Artificial Intelligence Internship
TASK 4: RECOMMENDATION SYSTEM

A simple movie recommendation system using two techniques:
1. Content-Based Filtering (based on genre similarity - cosine similarity)
2. Collaborative Filtering (based on user-user similarity from ratings)

No external dataset needed - a small sample dataset is included so the
script runs out of the box. Swap in a real dataset (e.g. MovieLens) for
production use.
"""

import math
from collections import defaultdict

# ----------------------------------------------------------------------
# Sample dataset
# ----------------------------------------------------------------------
movies = {
    "Inception": ["Sci-Fi", "Thriller", "Action"],
    "Interstellar": ["Sci-Fi", "Drama", "Adventure"],
    "The Dark Knight": ["Action", "Crime", "Thriller"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "Avengers: Endgame": ["Action", "Sci-Fi", "Adventure"],
    "La La Land": ["Romance", "Musical", "Drama"],
    "The Matrix": ["Sci-Fi", "Action"],
}

# user -> {movie: rating(1-5)}
user_ratings = {
    "Aryan": {"Inception": 5, "The Dark Knight": 4, "The Matrix": 5},
    "Priya": {"Titanic": 5, "The Notebook": 4, "La La Land": 5},
    "Rohit": {"Interstellar": 5, "Inception": 4, "Avengers: Endgame": 4},
}


# ----------------------------------------------------------------------
# 1) Content-Based Filtering
# ----------------------------------------------------------------------
def genre_vector(movie_genres, all_genres):
    return [1 if g in movie_genres else 0 for g in all_genres]


def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1))
    mag2 = math.sqrt(sum(b * b for b in v2))
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot / (mag1 * mag2)


def content_based_recommend(liked_movie, top_n=3):
    all_genres = sorted({g for genres in movies.values() for g in genres})
    target_vector = genre_vector(movies[liked_movie], all_genres)

    scores = []
    for movie, genres in movies.items():
        if movie == liked_movie:
            continue
        vec = genre_vector(genres, all_genres)
        sim = cosine_similarity(target_vector, vec)
        scores.append((movie, sim))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]


# ----------------------------------------------------------------------
# 2) Collaborative Filtering (user-based)
# ----------------------------------------------------------------------
def user_similarity(u1_ratings, u2_ratings):
    common = set(u1_ratings) & set(u2_ratings)
    if not common:
        return 0
    v1 = [u1_ratings[m] for m in common]
    v2 = [u2_ratings[m] for m in common]
    return cosine_similarity(v1, v2)


def collaborative_recommend(target_user, top_n=3):
    target_ratings = user_ratings[target_user]
    similarities = {}
    for other_user, ratings in user_ratings.items():
        if other_user == target_user:
            continue
        similarities[other_user] = user_similarity(target_ratings, ratings)

    scores = defaultdict(float)
    weight_sum = defaultdict(float)

    for other_user, sim in similarities.items():
        if sim <= 0:
            continue
        for movie, rating in user_ratings[other_user].items():
            if movie not in target_ratings:
                scores[movie] += sim * rating
                weight_sum[movie] += sim

    recommendations = [
        (movie, scores[movie] / weight_sum[movie])
        for movie in scores if weight_sum[movie] > 0
    ]
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]


if __name__ == "__main__":
    print("=== Content-Based Recommendations ===")
    liked = "Inception"
    print(f"Because you liked '{liked}':")
    for movie, score in content_based_recommend(liked):
        print(f"  {movie}  (similarity: {score:.2f})")

    print("\n=== Collaborative Filtering Recommendations ===")
    user = "Aryan"
    print(f"Recommended for {user}:")
    for movie, score in collaborative_recommend(user):
        print(f"  {movie}  (predicted score: {score:.2f})")
