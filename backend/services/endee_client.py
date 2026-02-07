import requests
import uuid

class EndeeClient:
    def __init__(self):
        # We define the base_url here so we can talk to Docker directly
        self.base_url = "http://localhost:8080"
        self.index_name = "resumes_endee"

    def initialize_collection(self):
        """Pure API version: No SDK, no Pydantic errors."""
        url = f"{self.base_url}/collections"
        payload = {
            "name": self.index_name,
            "dimension": 384,
            "space_type": "cosine"
        }
        try:
            # Check if index exists
            check = requests.get(f"{url}/{self.index_name}")
            if check.status_code == 200:
                print(f"--- Index '{self.index_name}' verified! ---")
            else:
                # Create it if it's missing
                requests.post(url, json=payload)
                print(f"--- SUCCESS: Index created via API! ---")
        except Exception as e:
            print(f"--- Connection Error: {e} ---")

    def check_health(self):
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False

    def insert_resume(self, filename, vector, metadata):
        """Matches your old project's logic but uses safe REST calls."""
        url = f"{self.base_url}/collections/{self.index_name}/points"
        payload = {
            "points": [{
                "id": str(uuid.uuid4()),
                "vector": vector,
                "meta": {"filename": filename, **metadata}
            }]
        }
        try:
            response = requests.put(url, json=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"--- Upsert Error: {e} ---")
            return False

    def search_resumes(self, query_vector, top_k=5):
        url = f"{self.base_url}/collections/{self.index_name}/query"
        payload = {"vector": query_vector, "top_k": top_k}
        try:
            response = requests.post(url, json=payload)
            return response.json() if response.status_code == 200 else []
        except:
            return []