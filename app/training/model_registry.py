from pathlib import Path
import joblib 
from app.training.config import MODEL_DIR
from app.training.training_results import TrainingResult

class ModelRegistry:

    def __init__(self):

        MODEL_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save_model(
            self,
            training_result:TrainingResult,
            filename : str = "random_forest.pkl",
    ) -> Path :

        model_path = MODEL_DIR/filename
        joblib.dump(
            training_result.model,
            model_path,
        )
        print(f"\nModel saved successfully.")
        print(f"Location : {model_path}")
        return model_path

    def load_model(
            self,
            filename:str = "random_forest.pkl",
    ):
        model_path = MODEL_DIR / filename
        if not model_path.exists():
            raise FileNotFoundError(
                f"Model not found: {model_path}"
            )

        return joblib.load(model_path)