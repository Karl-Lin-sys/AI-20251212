from pydantic import BaseModel
from typing import List, Optional

class ListingBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    area: float
    bedrooms: int
    location: str
    features: Optional[str] = None

class ListingCreate(ListingBase):
    pass

class Listing(ListingBase):
    id: int

    class Config:
        from_attributes = True

class PricePredictionRequest(BaseModel):
    area: float
    bedrooms: int
    location: str
    # dummy feature to simulate advanced model input
    feature_score: float = 0.5 

class PricePredictionResponse(BaseModel):
    estimated_price: float
    confidence: float

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    intent: str
