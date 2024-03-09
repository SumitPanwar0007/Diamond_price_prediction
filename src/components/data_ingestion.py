import os 
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from builtins import dataclass


#initialize data ingestion
@dataclass
class DataIngestionConfig:
    train_data_path= os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path =  os.path.join('artifacts','raw.csv')

##create a data ingestion class
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_dataIngestion(self):
        logging.info("data Ingestion start")
 
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstones.csv'))
            logging.info("database read as pandas dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train test split")
            train_set,test_set = train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv( self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("error occured in data ingestion")
