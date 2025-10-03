from core.Config import Config
from Streamlit import Page
from infra.GoogleCloudStorage import GoogleCloudStorage

import os
from dotenv import load_dotenv
load_dotenv()


if __name__=="__main__":
    try:
        config = Config(env_type=os.getenv("ENV")).get_env()
        # gcs = GoogleCloudStorage(
        #     project_id=config["GCP"]["GCP_PROJECT_ID"],
        #     bucket_name=config["GCP"]["BUCKET_NAME" ],
        #     resources_path=config["GCP"]["RESOURCES_PATH"]
        # )
        st = Page(config=config, storage=None)
        
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)