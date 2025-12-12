import pandas as pd
import numpy as np
import random

def generate_rental_data(n_samples=1000):
    locations = ['Xitun', 'Nantun', 'Beitun', 'Central', 'West']
    
    # Base price mapping (NTD/ping approx)
    loc_multiplier = {
        'Xitun': 1200, 
        'Nantun': 1000, 
        'Beitun': 900, 
        'Central': 800, 
        'West': 1100
    }
    
    data = []
    for _ in range(n_samples):
        loc = random.choice(locations)
        area = np.random.normal(30, 10) # 30 ping avg
        area = max(5, area)
        
        bedrooms = 1
        if area > 20: bedrooms = 2
        if area > 40: bedrooms = 3
        if area > 60: bedrooms = 4
        
        # Feature Engineering (noisy linear relationship)
        base_price = area * loc_multiplier[loc]
        bedroom_premium = bedrooms * 2000
        noise = np.random.normal(0, 3000)
        
        price = base_price + bedroom_premium + noise
        price = max(5000, int(price))
        
        features = []
        if random.random() > 0.5: features.append('lift')
        if random.random() > 0.5: features.append('security')
        if random.random() > 0.5: features.append('gym')
        if random.random() > 0.5: features.append('parking')
        
        data.append({
            'location': loc,
            'area': round(area, 1),
            'bedrooms': bedrooms,
            'price': price,
            'features': ",".join(features)
        })
        
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_rental_data()
    print(df.head())
    df.to_csv("rental_data.csv", index=False)
