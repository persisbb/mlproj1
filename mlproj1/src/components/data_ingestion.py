import os
import sys
from src.exception import CustomException
from ..logger import logging
import pandas as pd



from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass #called decorator - don't have to use init method, it will automatically create init method for us
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
          
            
            df = pd.read_csv(r'..\notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #to create a directory if it doesn't exist, if it already exists then it will not throw an error

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)#to save the raw data in the artifacts folder, index=False to avoid saving the index column, header=True to save the column names

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            print(os.path.exists(self.ingestion_config.raw_data_path))
            print(os.path.exists(self.ingestion_config.train_data_path))
            print(os.path.exists(self.ingestion_config.test_data_path))

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

                
            )

        except Exception as e:
            logging.info("Error occurred in data ingestion component")
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
