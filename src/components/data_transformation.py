from sklearn.impute import SimpleImputer               #Handling MIssing Values
from sklearn.preprocessing import StandardScaler         #Handling Features Scaling
from sklearn.preprocessing import OrdinalEncoder        #Ordinal encoding
##pipeline
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import sys,os
import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

## data transformation config:

@dataclass
class DataTransformatinconfig:
    preprocessor_ob_file_path = os.path.join('artifacts','preprocessor.pkl')

##Data Ingestioncongig class
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformatinconfig(
            
        )