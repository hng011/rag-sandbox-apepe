from google.cloud import storage

class GoogleCloudStorage:
    def __init__(self,
                 project_id: str,
                 bucket_name: str,
                 resources_path: str):
        
        self.storage_client = storage.Client(project=project_id)
        self.bucket_name = self.storage_client.bucket(bucket_name=bucket_name)        
        self.resources_path = resources_path 
        
    def upload(self, file_source: str, dest_blob: str):
        pass
    
    def list(self):
        pass

    def delete(self, blob_name):
        pass