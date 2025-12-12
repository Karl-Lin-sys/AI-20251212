# PropAI Assistant: Intelligent Rental Platform Backend

## Overview
**PropAI Assistant** is a microservices-ready backend system designed for the next generation of Smart Leasing Platforms (PropTech). It integrates **Machine Learning** for property valuation, **Recommendation Systems** for personalized matching, and **NLP** for automated tenant support.

This project was built to demonstrate core competencies for the **AI Engineer** role at **Create Future**.

## Key Features & Skill Application

| Feature | Tech Stack | Job Requirement Addressed |
| :--- | :--- | :--- |
| **Rent Estimator** | Python, `scikit-learn` (Random Forest) | *"Optimise models... proficient in Python and common ML libraries"* |
| **Smart Recommendations** | Content-based Filtering (Cosine Similarity) | *"Familiarity with recommendation systems"* |
| **Tenant Chatbot** | NLP Pipeline (Intent Classification, NER) | *"NLP technology... experience in Chatbot development"* |
| **API Gateway** | FastAPI, Pydantic, REST | *"RESTful API standards, Microservices"* |
| **Data Engine** | Pandas, NumPy | *"Data cleaning, feature engineering... extract value from unstructured data"* |

## Project Structure

```bash
prop_ai_assistant/
├── main.py                 # FastAPI Application (Entry Point)
├── ml_core/               
│   ├── price_model.py      # Random Forest Regression Model
│   ├── recommender.py      # Recommendation Engine
│   └── data_generator.py   # Synthetic Data Generation
├── nlp_core/
│   ├── bot.py              # Chatbot Agent Logic
│   └── processor.py        # Text Cleaning & Feature Extraction
└── requirements.txt        # Dependencies
```

## Setup & Running

### Prerequisites
- Python 3.9+
- Pip

### Quick Start
1.  **Clone the repository** (or download):
    ```bash
    git clone https://github.com/yourusername/prop-ai-assistant.git
    cd prop_ai_assistant
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Server**:
    ```bash
    uvicorn main:app --reload
    ```

4.  **Explore the API**:
    Open your browser to `http://127.0.0.1:8000/docs` to see the interactive Swagger UI.

## Usage Examples

### 1. Predict Rental Price
**POST** `/predict-rent`
```json
{
  "area": 35.5,
  "bedrooms": 2,
  "location": "Xitun",
  "feature_score": 0.8
}
```

### 2. Chat with AI
**POST** `/chat`
```json
{
  "user_id": "user_123",
  "message": "I want to find a 2 bedroom apartment in Xitun"
}
```

### 3. Get Recommendations
**GET** `/recommend-listings?features=gym%20parking%20near%20station`

## Future Roadmap
- [ ] Deploy to Cloud (AWS/GCP) using Docker.
- [ ] Integrate Llama-2/3 for advanced conversational capabilities.
- [ ] Add Time Series Analysis for market trend forecasting.
