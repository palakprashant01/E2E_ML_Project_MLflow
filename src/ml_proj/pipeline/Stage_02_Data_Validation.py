from ml_proj.config.configuration import ConfigManager
from ml_proj.components.data_validation import DataValidation
from ml_proj import logger

stage = 'Data Validation Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigManager()

        data_validation_configuration =  config.get_data_validation_configuration()
        data_validation = DataValidation(config=data_validation_configuration)
        data_validation.validate_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
        object = DataValidationTrainingPipeline()
        object.main()
        logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e
    