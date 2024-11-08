from ml_proj.config.configuration import ConfigManager
from ml_proj.components.model_trainer import ModelTrainer
from ml_proj import logger
from pathlib import Path

stage = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigManager()
        ModelTrainerConfiguration = config.get_model_trainer_configuration()
        ModelTrainerConfiguration = ModelTrainer(config = ModelTrainerConfiguration)
        ModelTrainerConfiguration.model_train()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
        object = ModelTrainerTrainingPipeline()
        object.main()
        logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e

