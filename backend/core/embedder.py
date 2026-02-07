import requests
import time

class OnlineEmbedder:
    def __init__(self, token: str):

        # We use the same model but call it via HF's infrastructure
        self.api_url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"
        self.headers = {"Authorization": f"Bearer {token}"}

    def generate_vector(self, text):
        if not text:
            return [0.0] * 384
            
        payload = {
            "inputs": [text], 
            "options": {"wait_for_model": True}
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=15)
            
            if response.status_code == 200:
                result = response.json()
                
                # Check for nested list structure [[...]]
                if isinstance(result, list) and len(result) > 0:
                    return result[0]
                return result
            else:
                print(f"HF API Error: {response.status_code} - {response.text}")
                return [0.0] * 384

   
        except requests.exceptions.RequestException as e:
            print(f"Connection Error to HF: {e}")
            return [0.0] * 384
            
     
        finally:
         
            pass