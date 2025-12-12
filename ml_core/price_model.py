import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
import joblib
import os
from .data_generator import generate_rental_data

MODEL_PATH = "ml_core/price_model.pkl"

class PriceModel:
    def __init__(self):
        self.model = None
        self.pipeline = None
        
    def train(self):
        # Generate data on the fly if file doesn't exist (or just always for demo)
        df = generate_rental_data(2000)
        
        X = df[['location', 'area', 'bedrooms']]
        y = df['price']
        
        # Preprocessing
        numeric_features = ['area', 'bedrooms']
        categorical_features = ['location']
        
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numeric_features),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
            ])
            
        self.pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
        ])
        
        self.pipeline.fit(X, y)
        print("Model trained.")
        
    def save(self):
        joblib.dump(self.pipeline, MODEL_PATH)
        
    def load(self):
        if os.path.exists(MODEL_PATH):
            self.pipeline = joblib.load(MODEL_PATH)
        else:
            print("Model not found, training new one...")
            self.train()
            self.save()
            
    def predict(self, location, area, bedrooms):
        if not self.pipeline:
            self.load()
            
        input_data = pd.DataFrame({
            'location': [location],
            'area': [area],
            'bedrooms': [bedrooms]
        })
        
        prediction = self.pipeline.predict(input_data)[0]
        return prediction

# Singleton instance
price_model = PriceModel()
