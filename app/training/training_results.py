from dataclasses import dataclass
import pandas as pd

@dataclass
class TrainingResult :

    model : object
    X_train : pd.DataFrame
    X_test :  pd.DataFrame

    y_train : pd.Series
    y_test : pd.Series

    train_predictions : pd.Series
    test_predictions : pd.Series