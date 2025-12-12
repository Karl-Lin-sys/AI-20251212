import random
from .processor import TextProcessor

class PropChatBot:
    def __init__(self):
        self.processor = TextProcessor()
        
    def predict_intent(self, text: str) -> str:
        # Simulating an Intent Classifier Model
        clean_text = self.processor.clean_text(text)
        
        if any(w in clean_text for w in ['price', 'cost', 'rent', 'valuation']):
            return "price_inquiry"
        elif any(w in clean_text for w in ['recommend', 'find', 'search', 'looking for', 'show me']):
            return "property_search"
        elif any(w in clean_text for w in ['help', 'support', 'contact']):
            return "support"
        else:
            return "chit_chat"

    def get_response(self, text: str, user_id: str) -> dict:
        intent = self.predict_intent(text)
        entities = self.processor.extract_entities(TextProcessor.clean_text(text))
        
        response_text = ""
        
        if intent == "price_inquiry":
            response_text = "I can help you estimate rental prices. Please provide the location, size (ping), and number of bedrooms."
            if entities:
                response_text += f" I see you're interested in {entities.get('location', 'an area')}."
                
        elif intent == "property_search":
            response_text = "I can recommend some listings! Tell me what features you are looking for (e.g., gym, parking, near station)."
            
        elif intent == "support":
            response_text = "Support team is available 9-18. How else can I assist you with our AI services?"
            
        else:
            responses = [
                "Hello! I am your AI Property Assistant.",
                "How can I help you with your property needs today?",
                "I can predict rent prices or recommend houses."
            ]
            response_text = random.choice(responses)
            
        return {
            "reply": response_text,
            "intent": intent,
            "entities": entities
        }

bot = PropChatBot()
