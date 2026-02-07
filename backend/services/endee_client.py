import requests
import uuid


class EndeeClient:
    def __init__(self):
        # The Dashboard is at /indexes/create, but the API is usually at /v1/indexes
        self.base_url = "http://localhost:8080/v1" 
        self.index_name = "resumes_endee"
        self.headers = {"Content-Type": "application/json"}

    def initialize_collection(self):
        url = f"{self.base_url}/collections"
        try:
            # Step 1: Check if it exists
            check = requests.get(f"{url}/{self.index_name}")
            
            if check.status_code == 200:
                print(f"--- Index '{self.index_name}' verified! ---")
            else:
                # Step 2: Create with explicit headers
                payload = {
                    "name": self.index_name,
                    "dimension": 384,
                    "space_type": "cosine"
                }
                response = requests.post(url, json=payload, headers=self.headers)
                
                if response.status_code in [200, 201]:
                    print(f"--- SUCCESS: Index '{self.index_name}' created via API! ---")
                else:
                    print(f"--- FAILED to create index: {response.text} ---")
        except Exception as e:
            print(f"--- Connection Error: {e} ---")

    def insert_resume(self, filename, vector, metadata):
        url = f"{self.base_url}/collections/{self.index_name}/points"
        payload = {
            "points": [{
                "id": str(uuid.uuid4()),
                "vector": vector,
                "meta": {"filename": filename, **metadata}
            }]
        }
        try:
            # Use headers here too!
            response = requests.put(url, json=payload, headers=self.headers)
            return response.status_code == 200
        except Exception as e:
            print(f"--- Upsert Error: {e} ---")
            return False