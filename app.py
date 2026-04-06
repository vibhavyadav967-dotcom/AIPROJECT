"""
Streamlit Web App for Movie/Book Recommender System
Host on: https://streamlit.io/cloud (FREE)
"""

import streamlit as st
import pandas as pd
from sample_data import create_sample_data
from recommender import CollaborativeRecommender, ContentBasedRecommender, HybridRecommender

# Page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎬 Movie Recommender System")
st.markdown("*AI-Powered Personalized Movie Recommendations*")
st.divider()

# Load data
@st.cache_resource
def load_data():
    movies_df, ratings_df = create_sample_data()
    return movies_df, ratings_df

@st.cache_resource
def create_recommenders(movies_df, ratings_df):
    collab = CollaborativeRecommender(ratings_df)
    content = ContentBasedRecommender(movies_df)
    hybrid = HybridRecommender(ratings_df, movies_df)
    return collab, content, hybrid

movies_df, ratings_df = load_data()
collab_rec, content_rec, hybrid_rec = create_recommenders(movies_df, ratings_df)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    rec_type = st.radio(
        "Choose Recommendation Type:",
        ["Collaborative Filtering", "Content-Based", "Hybrid"]
    )
    
    num_recs = st.slider("Number of recommendations:", 1, 10, 5)
    st.divider()
    
    st.markdown("### 📊 About This System")
    st.markdown("""
    - **Collaborative**: Users who rated items similarly
    - **Content-Based**: Similar movies to what you like
    - **Hybrid**: Combines both approaches
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    if rec_type == "Collaborative Filtering":
        st.subheader("🤝 Collaborative Filtering")
        st.markdown("Recommendations based on similar users' preferences")
        
        user_id = st.slider("Select User ID:", 1, 5, 1)
        
        if st.button("Get Recommendations", key="collab_btn"):
            recs = collab_rec.recommend(user_id, n_recommendations=num_recs)
            
            if recs:
                st.success(f"Top {len(recs)} recommendations for User {user_id}:")
                
                for idx, (item_id, score) in enumerate(recs, 1):
                    movie = movies_df[movies_df['item_id'] == item_id].iloc[0]
                    
                    with st.container():
                        col_num, col_title, col_score = st.columns([0.5, 2, 1])
                        with col_num:
                            st.markdown(f"**#{idx}**")
                        with col_title:
                            st.markdown(f"**{movie['title']}**")
                            st.caption(f"Genres: {movie['genres']}")
                        with col_score:
                            st.metric("Score", f"{score:.3f}")
                        st.divider()
            else:
                st.warning("No recommendations found for this user.")
    
    elif rec_type == "Content-Based":
        st.subheader("📚 Content-Based Filtering")
        st.markdown("Recommendations based on movie features and genres")
        
        selected_movie = st.selectbox(
            "Select a movie:",
            movies_df['title'].tolist()
        )
        
        if st.button("Find Similar Movies", key="content_btn"):
            movie_id = movies_df[movies_df['title'] == selected_movie]['item_id'].values[0]
            recs = content_rec.recommend(movie_id, n_recommendations=num_recs)
            
            if recs:
                st.success(f"Movies similar to '{selected_movie}':")
                
                for idx, (item_id, score) in enumerate(recs, 1):
                    movie = movies_df[movies_df['item_id'] == item_id].iloc[0]
                    
                    with st.container():
                        col_num, col_title, col_score = st.columns([0.5, 2, 1])
                        with col_num:
                            st.markdown(f"**#{idx}**")
                        with col_title:
                            st.markdown(f"**{movie['title']}**")
                            st.caption(f"Genres: {movie['genres']}")
                        with col_score:
                            st.metric("Similarity", f"{score:.3f}")
                        st.divider()
            else:
                st.warning("No similar movies found.")
    
    else:  # Hybrid
        st.subheader("⭐ Hybrid Recommendations")
        st.markdown("Best of both collaborative and content-based approaches")
        
        user_id = st.slider("Select User ID:", 1, 5, 1)
        collab_weight = st.slider("Collaborative Weight:", 0.0, 1.0, 0.6, 0.1)
        
        if st.button("Get Hybrid Recommendations", key="hybrid_btn"):
            recs = hybrid_rec.recommend(user_id, n_recommendations=num_recs, collab_weight=collab_weight)
            
            if recs:
                st.success(f"Top {len(recs)} personalized recommendations for User {user_id}:")
                
                for idx, (item_id, score) in enumerate(recs, 1):
                    movie = movies_df[movies_df['item_id'] == item_id].iloc[0]
                    
                    with st.container():
                        col_num, col_title, col_score = st.columns([0.5, 2, 1])
                        with col_num:
                            st.markdown(f"**#{idx}**")
                        with col_title:
                            st.markdown(f"**{movie['title']}**")
                            st.caption(f"Genres: {movie['genres']}")
                        with col_score:
                            st.metric("Score", f"{score:.3f}")
                        st.divider()
            else:
                st.warning("No recommendations found.")

with col2:
    st.subheader("📊 Dataset Stats")
    st.metric("Total Movies", len(movies_df))
    st.metric("Total Users", ratings_df['user_id'].nunique())
    st.metric("Total Ratings", len(ratings_df))
    st.metric("Avg Rating", f"{ratings_df['rating'].mean():.2f}")
    
    st.divider()
    
    st.subheader("🎓 Dataset")
    if st.checkbox("Show all movies"):
        st.dataframe(
            movies_df[['item_id', 'title', 'genres']],
            use_container_width=True
        )

# Footer
st.divider()
st.markdown("""
---
**Project**: AI Movie Recommender | **Student**: College Project
- Built with Streamlit, Python, scikit-learn
- Algorithms: Collaborative Filtering, Content-Based, Hybrid
- Data: Sample MovieLens-style dataset

[GitHub](#) | [Documentation](#) | [Contact](#)
""")
