import pandas as pd

from app.inference.predictor import Predictor
from app.training.config import DATASET_PATH, FEATURE_COLUMNS


def main():

    df = pd.read_csv(DATASET_PATH)

    predictor = Predictor()

    row = df.iloc[0]

    features = row[FEATURE_COLUMNS].to_dict()

    prediction = predictor.predict(features)

    print("=" * 60)
    print("MODEL VERIFICATION")
    print("=" * 60)

    print(f"Dataset Expert Score : {row['expert_score']:.6f}")
    print(f"Model Prediction     : {prediction:.6f}")
    print(f"Difference           : {abs(row['expert_score'] - prediction):.6f}")


if __name__ == "__main__":
    main()