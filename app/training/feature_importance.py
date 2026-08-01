import pandas as pd

from config import FEATURE_COLUMNS
from random_forest_trainer import RandomForestTrainer

class FeatureImportanceAnalyzer:

    def __init__(self):

        self.model = None

    def load_model(self):

        trainer = RandomForestTrainer()
        (
            self.model,
            _,_,_,_,_,_,
        ) = trainer.run()

    def analyzer(self):

        importance = pd.DataFrame(
            {
                "Feature" : FEATURE_COLUMNS,
                "Importance" : self.model.feature_importances_,
            }
        )

        importance = importance.sort_values(
            by="Importance",
            ascending = False
        )

        print("=" * 60)
        print("Feature Importance")
        print("=" * 60)

        print(importance)
        return importance

    def run(self):

        self.load_model()
        return self.analyzer()

def main():
    analyzer = FeatureImportanceAnalyzer()
    analyzer.run()

if __name__  == "__main__":
    main()