# Movie/Book Recommender System

A moderate-level AI project implementing multiple recommendation algorithms.

## Features

### 1. **Collaborative Filtering**
- Finds similar users based on rating patterns
- Recommends items that similar users rated highly
- Best for: Discovering new items based on community preferences
- Algorithm: User-to-user similarity using cosine distance

### 2. **Content-Based Filtering**
- Recommends items based on item features (genres, descriptions)
- Similar items to what user already likes
- Best for: Consistent recommendations in same genre/style
- Algorithm: TF-IDF vectorization + cosine similarity

### 3. **Hybrid Approach**
- Combines collaborative and content-based methods
- Balances discovery with consistency
- Best for: Production systems requiring diverse & relevant recommendations

## Project Structure

```
movie_recommender/
├── recommender.py          # Core algorithms
├── sample_data.py          # Generate test data
├── demo.py                 # Example usage
├── requirements.txt        # Dependencies
├── data/
│   ├── movies.csv         # Movie metadata
│   └── ratings.csv        # User ratings
└── README.md
```

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### 1. Generate Sample Data
```bash
python sample_data.py
```

### 2. Run Demo
```bash
python demo.py
```

### 3. Use in Your Code
```python
from recommender import CollaborativeRecommender
import pandas as pd

# Load your data
ratings_df = pd.read_csv('data/ratings.csv')

# Create recommender
recommender = CollaborativeRecommender(ratings_df)

# Get recommendations
recommendations = recommender.recommend(user_id=1, n_recommendations=5)
for item_id, score in recommendations:
    print(f"Item {item_id}: {score:.4f}")
```

## Key Concepts Covered

- **Matrix Operations**: User-item rating matrices
- **Similarity Metrics**: Cosine similarity, TF-IDF vectorization
- **Data Structures**: DataFrames, sparse matrices
- **Algorithms**: Collaborative filtering, content-based filtering
- **Evaluation**: Basic recommendation scoring

## Real Datasets to Extend This

1. **MovieLens** (https://grouplens.org/datasets/movielens/)
   - 100K to 25M ratings
   - User-friendly format
   
2. **Book Crossing** (http://www2.informatik.uni-freiburg.de/~cziegler/BX/)
   - 1.1M book ratings
   - Book metadata included

3. **IMDb** (https://www.imdb.com/interfaces/)
   - Large movie database
   - Requires additional formatting

## Improvements for Production

- [ ] Add rating normalization
- [ ] Implement matrix factorization (SVD)
- [ ] Add cold-start problem handling
- [ ] Use deep learning (embeddings)
- [ ] Implement evaluation metrics (MAE, RMSE, Precision@K)
- [ ] Add real-time feedback loop
- [ ] Cache recommendations for performance

## Learning Resources

- Coursera: "Machine Learning" by Andrew Ng
- "Recommender Systems Handbook" (open resource)
- Papers on matrix factorization & deep learning recommendations

---

Happy recommending! 🎬📚
