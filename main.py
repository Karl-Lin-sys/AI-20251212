from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from . import database, schemas
from .ml_core.price_model import price_model
from .ml_core.recommender import recommender
from .nlp_core.bot import bot

# Initialize Database
database.Base.metadata.create_all(bind=database.engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load ML models on startup
    print("Loading ML Models...")
    try:
        price_model.load()
        # Recommender init trains on dummy data automatically
        print("Models loaded successfully.")
    except Exception as e:
        print(f"Error loading models: {e}")
    yield
    print("Shutting down...")

app = FastAPI(
    title="PropAI Assistant",
    description="AI-powered Backend for Smart Leasing Platform",
    version="1.0.0",
    lifespan=lifespan
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Create Future PropTech AI API",
        "endpoints": ["/predict-rent", "/recommend-listings", "/chat"]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "PropTech AI"}

# --- AI Endpoints ---

@app.post("/predict-rent", response_model=schemas.PricePredictionResponse, tags=["AI Services"])
def predict_rent(request: schemas.PricePredictionRequest):
    """
    Predict rental price using Random Forest Regressor.
    """
    try:
        price = price_model.predict(request.location, request.area, request.bedrooms)
        return {"estimated_price": round(price, 2), "confidence": 0.85} # Mock confidence
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/recommend-listings", tags=["AI Services"])
def recommend_listings(features: str, top_n: int = 3):
    """
    Recommend listings based on feature description using Cosine Similarity.
    """
    results = recommender.recommend(features, top_n=top_n)
    return results

@app.post("/chat", response_model=schemas.ChatResponse, tags=["NLP Services"])
def chat(request: schemas.ChatRequest):
    """
    Chat with the AI Assistant (Intent Classification & Entity Extraction).
    """
    response = bot.get_response(request.message, request.user_id)
    return response

@app.post("/admin/retrain-model", tags=["Admin"])
def retrain_model(background_tasks: BackgroundTasks):
    """
    Trigger model retraining in background.
    """
    background_tasks.add_task(price_model.train)
    return {"message": "Model retraining started in background."}
