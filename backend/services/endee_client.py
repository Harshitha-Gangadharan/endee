import requests
import uuid
from endee import Endee, Precision

class EndeeClient:
    def __init__(self):
        self.client = Endee()
        self.index_name = "resumes_endee"
        self.base_url = "http://localhost:8080" # Match your old project

    def initialize_collection(self):
        """Matches your old project's startup logic."""
        try:
            try:
                self.client.get_index(name=self.index_name)
                print(f"--- Index '{self.index_name}' verified! ---")
            except Exception:
                print(f"--- Creating {self.index_name}... ---")
                self.client.create_index(
                    name=self.index_name,
                    dimension=384,
                    space_type="cosine",
                    precision=Precision.INT8D
                )
        except Exception as e:
            print(f"--- Initialization Error: {e} ---")

    def check_health(self):
        """Bypasses SDK using Requests (Safe from Pydantic errors)"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False

    def insert_resume(self, filename, vector, metadata):
        """Matches your working 'upsert' pattern."""
        try:
            index = self.client.get_index(name=self.index_name)
            data_to_upsert = [{
                "id": str(uuid.uuid4()),  
                "vector": vector,         
                "meta": {                 
                    "filename": filename,
                    **metadata            
                }
            }]
            index.upsert(data_to_upsert)
            return True
        except Exception as e:
            print(f"--- Upsert Error: {e} ---")
            return False