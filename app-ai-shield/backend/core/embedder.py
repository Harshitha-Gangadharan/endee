import requests

class OnlineEmbedder:
    def __init__(self, token):
        # This is the EXACT URL from your working project
        self.api_url = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"
        self.headers = {"Authorization": f"Bearer {token}"}

    def generate_vector(self, text):
        if not text:
            return [0.0] * 384
            
        payload = {
            "inputs": text,
            "options": {"wait_for_model": True}
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=20)
            
            if response.status_code == 200:
                result = response.json()
                
                # The pipeline version returns a list of floats directly: [0.1, 0.2, ...]
                # or a nested list [[0.1, 0.2, ...]]. We handle both:
                if isinstance(result, list) and len(result) > 0:
                    return result[0] if isinstance(result[0], list) else result
                return result
            else:
                print(f"HF API Error: {response.status_code} - {response.text}")
                return [0.0] * 384
        except Exception as e:
            print(f"Connection Error: {e}")
            return [0.0] * 384