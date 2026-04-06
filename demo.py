"""
Demo script showing how to use the Movie/Book Recommender System
"""

import pandas as pd
from sample_data import create_sample_data
from recommender import CollaborativeRecommender, ContentBasedRecommender, HybridRecommender


def print_recommendations(title, recommendations, items_df):
    """Pretty print recommendations."""
    print("\n" + "="*60)
    print(title)
    print("="*60)
    
    if not recommendations:
        print("No recommendations found.")
        return
    
    for idx, (item_id, score) in enumerate(recommendations, 1):
        item_info = items_df[items_df['item_id'] == item_id].iloc[0]
        print(f"{idx}. {item_info['title']} (ID: {item_id})")
        print(f"   Score: {score:.4f}")
        print(f"   Genres: {item_info['genres']}")
        print()


def main():
    print("🎬 Movie/Book Recommender System Demo\n")
    
    # Load data
    movies_df, ratings_df = create_sample_data()
    
    # Initialize recommenders
    collab_rec = CollaborativeRecommender(ratings_df)
    content_rec = ContentBasedRecommender(movies_df)
    hybrid_rec = HybridRecommender(ratings_df, movies_df)
    
    # Test recommendations for User 1
    user_id = 1
    print(f"Generating recommendations for User {user_id}...")
    
    # Collaborative Filtering
    collab_recs = collab_rec.recommend(user_id, n_recommendations=3)
    print_recommendations(
        "COLLABORATIVE FILTERING - Users like you rated these highly:",
        collab_recs,
        movies_df
    )
    
    # Content-Based (based on first movie)
    first_movie_id = movies_df.iloc[0]['item_id']
    content_recs = content_rec.recommend(first_movie_id, n_recommendations=3)
    print_recommendations(
        f"CONTENT-BASED - Similar to '{movies_df.iloc[0]['title']}':",
        content_recs,
        movies_df
    )
    
    # Hybrid approach
    hybrid_recs = hybrid_rec.recommend(user_id, n_recommendations=3)
    print_recommendations(
        "HYBRID RECOMMENDATIONS (Best of both methods):",
        hybrid_recs,
        movies_df
    )
    
    # Display user's watch history
    print("\n" + "="*60)
    print(f"User {user_id}'s Watch History:")
    print("="*60)
    user_history = ratings_df[ratings_df['user_id'] == user_id]
    for _, row in user_history.iterrows():
        movie = movies_df[movies_df['item_id'] == row['item_id']].iloc[0]
        rating_stars = "[" + "*" * int(row['rating']) + "]"
        print(f"[OK] {movie['title']} - Rating: {rating_stars}")
    
    print("\n" + "="*60)
    print("Demo Complete!")


if __name__ == '__main__':
    main()
