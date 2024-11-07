import os
from ml_proj import logger
from ml_proj.entity.config_entity import DataValidationConfiguration
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfiguration):
        self.config = config
    
    def validate_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_directory)
            all_columns = list(data.columns) 

            entire_schema = self.config.entire_schema.keys()

            for col in all_columns: #Compare with columns in the schema
                if col not in entire_schema:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e
        
    