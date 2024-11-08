from src.ml_proj import logger
from ml_proj.pipeline.Stage_01_Data_Ingestion import DataIngestionTrainingPipeline
from ml_proj.pipeline.Stage_02_Data_Validation import DataValidationTrainingPipeline
from ml_proj.pipeline.Stage_03_Data_Transformation import DataTransformationTrainingPipeline
from ml_proj.pipeline.Stage_04_Model_Trainer import ModelTrainerTrainingPipeline

stage = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
    object = DataIngestionTrainingPipeline()
    object.main()
    logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

stage = "Data Validation Stage"

try:
    logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
    object = DataValidationTrainingPipeline()
    object.main()
    logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

stage = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
    object = DataTransformationTrainingPipeline()
    object.main()
    logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

stage = "Model Trainer Stage"

try:
    logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
    object = ModelTrainerTrainingPipeline()
    object.main()
    logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e