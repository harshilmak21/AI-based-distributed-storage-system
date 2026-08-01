import pandas as  pd
from app.training.config import FEATURE_COLUMNS
from app.training.model_registry import ModelRegistry

class Predictor:
    def __init__(self):

        registry = ModelRegistry()
        self.model = registry.load_model()

    def predict(self,featres : dict) -> float:
        input_df = pd.DataFrame(
            [featres],
            columns=FEATURE_COLUMNS,
        )

        predictions = self.model.predict(input_df)
        return float(predictions[0])