import requests
import time

class OnlineEmbedder:
    def __init__(self, token: str):
        # We use the same model but call it via HF's infrastructure
        self.api_url = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
        self.headers = {"Authorization": f"Bearer {token}"}

    def generate_vector(self, text: str):
        if not text:
            return [0.0] * 384
            
        payload = {
            "inputs": text,
            "options": {"wait_for_model": True}
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                # API usually returns a list of floats for feature extraction
                return result
            else:
                print(f"HF API Error: {response.status_code} - {response.text}")
                return [0.0] * 384
        except Exception as e:
            print(f"Connection Error: {e}")
            return [0.0] * 384