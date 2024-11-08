#Create components
import os
from ml_proj import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from ml_proj.entity.config_entity import DataTransformationConfiguration

class DataTransformation:
    def __init__(self, config: DataTransformationConfiguration):
        self.config = config

        #This data is already clean, else we would need to perform all kinds of EDA in ML cycle along with different data transformation techniques like Scaler, PCA, etc.

    def train_test_split_data(self):
        data = pd.read_csv(self.config.data_path)

        #Split data into training and testing data: using 75-25 ratio
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_directory, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_directory, "test.csv"), index = False)

        logger.info("The data has been split into training and test data sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)