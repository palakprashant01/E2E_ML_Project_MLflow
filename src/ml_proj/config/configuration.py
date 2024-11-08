from ml_proj.constants import *
from ml_proj.utils.common import read_yaml, create_directories
from ml_proj.entity.config_entity import (DataIngestionConfiguration, DataValidationConfiguration, DataTransformationConfiguration, ModelTrainerConfig)

class ConfigManager:
    def __init__(
            self,
            config_filepath = config_file,
            params_filepath = params_file,
            schema_filepath = schema_file):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_source])

    def get_data_ingestion_configuration(self) -> DataIngestionConfiguration:
        configuration = self.config.data_ingestion
        create_directories([configuration.root_directory])

        data_ingestion_configuration = DataIngestionConfiguration(
            root_directory= configuration.root_directory,
            source_URL= configuration.source_URL,
            local_data= configuration.local_data,
            unzip_directory=configuration.unzip_directory
        )
        return data_ingestion_configuration

    def get_data_validation_configuration(self) -> DataValidationConfiguration:
        configuration = self.config.data_validation
        print("Configuration Root Directory:", configuration.root_directory)
        schema = self.schema.COLUMNS
        
        # Correct the call to create_directories
        create_directories([configuration.root_directory])

        data_validation_configuration = DataValidationConfiguration(
            root_directory=configuration.root_directory,
            status_file=configuration.status_file,
            unzip_data_directory=configuration.unzip_data_directory,
            entire_schema=schema,
        )
        return data_validation_configuration

    def get_data_transformation_configuration(self) -> DataTransformationConfiguration:
        configuration = self.config.data_transformation
        
        # Correct the call to create_directories
        create_directories([configuration.root_directory])

        data_transformation_configuration = DataTransformationConfiguration(
            root_directory=configuration.root_directory,
            data_path=configuration.data_path,
        )
        return data_transformation_configuration
    
    def get_model_trainer_configuration(self) -> ModelTrainerConfig:
        configuration = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        # Correct the call to create_directories
        create_directories([configuration.root_directory])

        model_trainer_configuration = ModelTrainerConfig(
            root_directory=configuration.root_directory,
            train_data_path=configuration.train_data_path,
            test_data_path=configuration.test_data_path,
            model_name = configuration.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name

        )
        return model_trainer_configuration
        
    
