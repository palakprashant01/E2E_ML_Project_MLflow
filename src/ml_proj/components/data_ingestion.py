import os
import urllib.request as request #to retrieve and download data from the URL
import zipfile #to unzip data
from ml_proj import logger
from ml_proj.utils.common import size
from pathlib import Path
from ml_proj.entity.config_entity import DataIngestionConfiguration

class DataIngestion:
    def __init__(self, config: DataIngestionConfiguration):
        self.config = config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data
            )
            logger.info(f"{filename} download with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {size(Path(self.config.local_data))}")
    
    def extract_zip(self):
        #This function extracts the zip file into the data directory with None return type
        unzip_path = self.config.unzip_directory
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data, 'r') as zip_reference:
            zip_reference.extractall(unzip_path)