from endee import Endee, Precision
import uuid

class EndeeClient:
    def __init__(self):
        # The SDK handles the /v1/ path internally
        self.client = Endee() 
        self.index_name = "resumes_endee"

    def initialize_collection(self):
        """SDK Version of the startup logic."""
        try:
            try:
                # Check if index exists
                self.client.get_index(name=self.index_name)
                print(f"--- Index '{self.index_name}' verified via SDK! ---")
            except Exception:
                # Create if missing
                print(f"--- Creating {self.index_name} via SDK... ---")
                self.client.create_index(
                    name=self.index_name,
                    dimension=384,
                    space_type="cosine",
                    precision=Precision.INT8D
                )
                print(f"--- SUCCESS: Index created! ---")
        except Exception as e:
            print(f"--- SDK Initialization Error: {e} ---")

    def insert_resume(self, filename, vector, metadata):
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
            
            # 1. Standard SDK call (keep 'upsert')
            index.upsert(data_to_upsert)
            
            # 2. THE FIX: Force the engine to commit the points to the index
            # This matches the 'Autosave check' we saw in your Docker logs
            self.client.save_index(name=self.index_name)
            
            print(f"--- SDK Success & Committed: {filename} ---")
            return True
        except Exception as e:
            print(f"--- SDK Upsert Error: {e} ---")
            return False

    def search_resumes(self, query_vector, top_k=5):
        """
        Retrieves the most similar resumes based on the search query.
        """
        try:
            # Get the index object
            index = self.client.get_index(name=self.index_name)
            
            # Using ef=128 to ensure high accuracy for your demo
            results = index.query(
                vector=query_vector,
                top_k=top_k,
                ef=128,
                include_vectors=False  # We only need the metadata/filename
            )
            
            print(f"--- Search successful: Found {len(results)} matches ---")
            return results
        except Exception as e:
            print(f"--- Search Error: {e} ---")
            return []