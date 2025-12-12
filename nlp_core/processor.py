import re

class TextProcessor:
    @staticmethod
    def clean_text(text: str) -> str:
        # Simulate Data Cleaning / Feature Engineering
        # 1. Lowercase
        text = text.lower()
        # 2. Remove special chars
        text = re.sub(r'[^a-z0-9\s]', '', text)
        # 3. Collapse whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    @staticmethod
    def extract_entities(text: str) -> dict:
        # Rule-based entity extraction (Simulating NER)
        entities = {}
        
        # Extract location
        locations = ['xitun', 'nantun', 'beitun', 'central', 'west']
        for loc in locations:
            if loc in text:
                entities['location'] = loc.capitalize()
                
        # Extract beds
        # matches "2 bed", "2 bedroom", "2 br"
        bed_match = re.search(r'(\d+)\s*(bed|br|room)', text)
        if bed_match:
            entities['bedrooms'] = int(bed_match.group(1))
            
        return entities
