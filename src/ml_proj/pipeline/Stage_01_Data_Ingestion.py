from ml_proj.config.configuration import ConfigManager
from ml_proj.components.data_ingestion import DataIngestion
from ml_proj import logger

stage = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configuration = ConfigManager()
        data_ingestion_configuration = configuration.get_data_ingestion_configuration()
        data_ingestion = DataIngestion(config = data_ingestion_configuration)
        data_ingestion.download_data()
        data_ingestion.extract_zip()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
        object = DataIngestionTrainingPipeline()
        object.main()
        logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e