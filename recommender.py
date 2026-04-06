"""
Movie/Book Recommender System
Implements both Collaborative Filtering and Content-Based recommendations
"""

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class CollaborativeRecommender:
    """
    Recommends items based on user ratings similarity.
    Users who rated items similarly will get similar recommendations.
    """
    
    def __init__(self, ratings_df):
        """
        Args:
            ratings_df: DataFrame with columns ['user_id', 'item_id', 'rating']
        """
        self.ratings_df = ratings_df
        # Create user-item matrix (rows: users, columns: items, values: ratings)
        self.user_item_matrix = ratings_df.pivot_table(
            index='user_id',
            columns='item_id',
            values='rating'
        )
        # Fill NaN values with 0 (no rating)
        self.user_item_matrix = self.user_item_matrix.fillna(0)
        
        # Calculate user-to-user similarity using cosine similarity
        self.user_similarity = cosine_similarity(self.user_item_matrix)
        self.user_similarity_df = pd.DataFrame(
            self.user_similarity,
            index=self.user_item_matrix.index,
            columns=self.user_item_matrix.index
        )
    
    def recommend(self, user_id, n_recommendations=5):
        """
        Recommend items to a user based on similar users' ratings.
        
        Args:
            user_id: Target user ID
            n_recommendations: Number of items to recommend
            
        Returns:
            List of recommended item IDs with scores
        """
        if user_id not in self.user_similarity_df.index:
            return []
        
        # Get similar users (excluding the user themselves)
        similar_users = self.user_similarity_df[user_id].sort_values(ascending=False)[1:]
        
        # Get items rated by similar users but not by this user
        user_rated = set(self.ratings_df[self.ratings_df['user_id'] == user_id]['item_id'])
        
        # Calculate weighted scores for unrated items
        recommendations = {}
        for similar_user in similar_users.head(10).index:
            similar_user_ratings = self.ratings_df[self.ratings_df['user_id'] == similar_user]
            
            for _, row in similar_user_ratings.iterrows():
                item_id = row['item_id']
                rating = row['rating']
                similarity = similar_users[similar_user]
                
                if item_id not in user_rated:
                    if item_id not in recommendations:
                        recommendations[item_id] = []
                    recommendations[item_id].append(rating * similarity)
        
        # Average scores and sort
        recommendations = {
            item: sum(scores) / len(scores)
            for item, scores in recommendations.items()
        }
        
        sorted_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        return sorted_recs[:n_recommendations]


class ContentBasedRecommender:
    """
    Recommends items based on item features/descriptions.
    Similar items will be recommended to users who liked an item.
    """
    
    def __init__(self, items_df):
        """
        Args:
            items_df: DataFrame with columns ['item_id', 'title', 'description', 'genres']
        """
        self.items_df = items_df
        
        # Combine text features for similarity calculation
        self.items_df['combined_features'] = (
            self.items_df['genres'].fillna('') + ' ' + 
            self.items_df['description'].fillna('')
        )
        
        # Convert text to TF-IDF vectors
        self.tfidf = TfidfVectorizer(max_features=100, stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.items_df['combined_features'])
        
        # Calculate item-to-item similarity
        self.item_similarity = cosine_similarity(self.tfidf_matrix)
        self.item_similarity_df = pd.DataFrame(
            self.item_similarity,
            index=self.items_df['item_id'],
            columns=self.items_df['item_id']
        )
    
    def recommend(self, item_id, n_recommendations=5):
        """
        Recommend similar items based on content features.
        
        Args:
            item_id: Target item ID
            n_recommendations: Number of items to recommend
            
        Returns:
            List of recommended item IDs with similarity scores
        """
        if item_id not in self.item_similarity_df.index:
            return []
        
        # Get similar items (excluding the item itself)
        similar_items = self.item_similarity_df[item_id].sort_values(ascending=False)[1:]
        
        recommendations = [
            (item, score) for item, score in similar_items.head(n_recommendations).items()
        ]
        
        return recommendations


class HybridRecommender:
    """
    Combines Collaborative and Content-Based filtering for better recommendations.
    """
    
    def __init__(self, ratings_df, items_df):
        self.collaborative = CollaborativeRecommender(ratings_df)
        self.content_based = ContentBasedRecommender(items_df)
        self.items_df = items_df
    
    def recommend(self, user_id, n_recommendations=5, collab_weight=0.6):
        """
        Hybrid recommendation combining two approaches.
        
        Args:
            user_id: Target user ID
            n_recommendations: Number of items to recommend
            collab_weight: Weight for collaborative filtering (0-1)
            
        Returns:
            List of recommended items with combined scores
        """
        collab_recs = self.collaborative.recommend(user_id, n_recommendations * 2)
        content_recs = self.content_based.recommend(
            self.items_df.iloc[0]['item_id'],
            n_recommendations * 2
        )
        
        # Combine scores
        combined = {}
        for item_id, score in collab_recs:
            combined[item_id] = score * collab_weight
        
        for item_id, score in content_recs:
            if item_id in combined:
                combined[item_id] += score * (1 - collab_weight)
            else:
                combined[item_id] = score * (1 - collab_weight)
        
        sorted_recs = sorted(combined.items(), key=lambda x: x[1], reverse=True)
        return sorted_recs[:n_recommendations]
