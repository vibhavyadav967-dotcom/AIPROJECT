"""
Generate sample movie/book data for testing the recommender system.
In production, use real datasets like MovieLens, BookCrossing, etc.
"""

import pandas as pd
import numpy as np


def create_sample_data():
    """Create sample movie and ratings data."""
    
    # Sample movies
    movies = {
        'item_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'title': [
            'The Matrix',
            'Inception',
            'Interstellar',
            'The Dark Knight',
            'Pulp Fiction',
            'Forrest Gump',
            'The Shawshank Redemption',
            'Fight Club',
            'Gladiator',
            'Avatar'
        ],
        'genres': [
            'Sci-Fi, Action',
            'Sci-Fi, Thriller',
            'Sci-Fi, Drama',
            'Action, Crime',
            'Crime, Drama',
            'Drama, Comedy',
            'Drama',
            'Drama, Thriller',
            'Action, Drama',
            'Sci-Fi, Adventure'
        ],
        'description': [
            'A hacker discovers reality is a simulation controlled by machines',
            'A thief who steals corporate secrets through dreams',
            'Explorers travel through a wormhole to save humanity',
            'Batman fights a criminal mastermind in Gotham City',
            'Multiple stories intertwine in Los Angeles underworld',
            'A simple man witnesses key historical events in 20th century',
            'Two prison inmates bond and plan their escape',
            'An underground fight club becomes a social network',
            'A Roman general fights to survive as a slave',
            'A paraplegic marine battles in an alien world'
        ]
    }
    
    # Sample ratings
    ratings_data = [
        # User 1
        {'user_id': 1, 'item_id': 1, 'rating': 5},
        {'user_id': 1, 'item_id': 2, 'rating': 4},
        {'user_id': 1, 'item_id': 3, 'rating': 5},
        {'user_id': 1, 'item_id': 8, 'rating': 4},
        
        # User 2
        {'user_id': 2, 'item_id': 1, 'rating': 5},
        {'user_id': 2, 'item_id': 2, 'rating': 5},
        {'user_id': 2, 'item_id': 10, 'rating': 4},
        {'user_id': 2, 'item_id': 9, 'rating': 3},
        
        # User 3
        {'user_id': 3, 'item_id': 5, 'rating': 5},
        {'user_id': 3, 'item_id': 4, 'rating': 4},
        {'user_id': 3, 'item_id': 6, 'rating': 3},
        {'user_id': 3, 'item_id': 8, 'rating': 5},
        
        # User 4
        {'user_id': 4, 'item_id': 6, 'rating': 5},
        {'user_id': 4, 'item_id': 7, 'rating': 5},
        {'user_id': 4, 'item_id': 5, 'rating': 4},
        {'user_id': 4, 'item_id': 9, 'rating': 3},
        
        # User 5
        {'user_id': 5, 'item_id': 1, 'rating': 4},
        {'user_id': 5, 'item_id': 3, 'rating': 5},
        {'user_id': 5, 'item_id': 2, 'rating': 4},
        {'user_id': 5, 'item_id': 8, 'rating': 4},
    ]
    
    movies_df = pd.DataFrame(movies)
    ratings_df = pd.DataFrame(ratings_data)
    
    return movies_df, ratings_df


if __name__ == '__main__':
    movies_df, ratings_df = create_sample_data()
    
    # Save to CSV for later use
    movies_df.to_csv('data/movies.csv', index=False)
    ratings_df.to_csv('data/ratings.csv', index=False)
    
    print("Sample data created successfully!")
    print(f"\nMovies ({len(movies_df)} total):")
    print(movies_df)
    print(f"\nRatings ({len(ratings_df)} total):")
    print(ratings_df)
