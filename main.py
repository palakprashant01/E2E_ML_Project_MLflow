from src.ml_proj import logger
from ml_proj.pipeline.Stage_01_Data_Ingestion import DataIngestionTrainingPipeline

stage = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
    object = DataIngestionTrainingPipeline()
    object.main()
    logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e