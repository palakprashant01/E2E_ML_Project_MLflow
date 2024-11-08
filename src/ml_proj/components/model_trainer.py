#Define components
import pandas as pd
import os
from ml_proj import logger
from sklearn.linear_model import ElasticNet
import joblib
from ml_proj.entity.config_entity import ModelTrainerConfig

#Create components

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    def model_train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        training_x = train_data.drop([self.config.target_column], axis = 1)
        test_x = test_data.drop([self.config.target_column], axis = 1)

        training_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        lr = ElasticNet(alpha = self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(training_x, training_y)


        joblib.dump(lr, os.path.join(self.config.root_directory, self.config.model_name))
        