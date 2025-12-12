import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .data_generator import generate_rental_data

class Recommender:
    def __init__(self):
        self.df = generate_rental_data(500) # Serve as our "database" of listings
        self.vectorizer = TfidfVectorizer()
        
        # Creating a "content" string for each listing combining features and location
        self.df['content'] = self.df['features'] + " " + self.df['location'] + " " + self.df['bedrooms'].astype(str) + "bed"
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['content'])
        
    def recommend(self, features_query, top_n=3):
        # Convert user query (e.g., "features I want") into vector
        query_vec = self.vectorizer.transform([features_query])
        
        # Compute cosine similarity
        cosine_sim = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # Get top matches
        indices = cosine_sim.argsort()[-top_n:][::-1]
        
        results = self.df.iloc[indices].copy()
        results['score'] = cosine_sim[indices]
        
        return results.to_dict(orient='records')

# Singleton
recommender = Recommender()
