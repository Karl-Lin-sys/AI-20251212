from fastapi.testclient import TestClient
from .main import app, lifespan
from .ml_core.price_model import price_model
import contextlib

client = TestClient(app)

def test_api():
    # Force load models since TestClient doesn't trigger lifespan automatically in all versions or simple usage?
    # Actually TestClient normally handles lifespan if used as context context manager.
    # But for simplicity, let's manually trigger load or just rely on the calls if we did it right.
    # Best way:
    with TestClient(app) as client:
        # 1. Health Check
        response = client.get("/health")
        assert response.status_code == 200
        print("Health Check: PASS")

        # 2. Train Model (via startup) - check if prediction works
        # Note: Model loading happened in startup
        
        # Predict Rent
        payload = {
            "area": 30.0,
            "bedrooms": 2,
            "location": "Xitun",
            "feature_score": 0.5
        }
        response = client.post("/predict-rent", json=payload)
        assert response.status_code == 200
        data = response.json()
        print(f"Prediction: {data['estimated_price']} (Confidence: {data['confidence']})")
        assert "estimated_price" in data
        print("Prediction API: PASS")

        # 3. Chat
        chat_payload = {
            "user_id": "test_user",
            "message": "I want to rent a 2 bedroom apartment in Xitun"
        }
        response = client.post("/chat", json=chat_payload)
        assert response.status_code == 200
        data = response.json()
        print(f"Chat Reply: {data['reply']}")
        assert data['intent'] in ["property_search", "price_inquiry"]
        print("Chat API: PASS")

        # 4. Recommend
        response = client.get("/recommend-listings?features=gym%20parking&top_n=2")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        print(f"Recommendations returned: {len(data)}")
        print("Recommendation API: PASS")

if __name__ == "__main__":
    print("Starting Verification...")
    test_api()
    print("ALL TESTS PASSED")
