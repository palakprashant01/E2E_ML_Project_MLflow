from ml_proj.config.configuration import ConfigManager
from ml_proj.components.data_transformation import DataTransformation
from ml_proj import logger
from pathlib import Path

stage = 'Data Transformation Stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    #Reading and splitting out the status only to get the boolean values
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                config = ConfigManager()
                data_transformation_configuration = config.get_data_transformation_configuration()
                data_transformation = DataTransformation(config = data_transformation_configuration)
                data_transformation.train_test_split_data()
            else:
                raise Exception("Your data schema is invalid!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {stage} started <<<<<<<<")
        object = DataTransformationTrainingPipeline()
        object.main()
        logger.info(f">>>>>>>> stage {stage} completed <<<<<<<<\n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e


