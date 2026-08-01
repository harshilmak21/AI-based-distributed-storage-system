from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score,
)

from random_forest_trainer import RandomForestTrainer

class ModelEvaluator :

    def __init__(self):

        self.model= None
        self.y_test = None
        self.predictions = None
        self.X_train = None
        self.y_train = None

        self.train_predictions = None

    def load_model_outputs(self):

        trainer = RandomForestTrainer()

        (
            self.model,
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
            self.train_predictions,
            self.predictions,
        ) = trainer.run()

    def evaluate(self):

        mae = mean_absolute_error(
            self.y_test,
            self.predictions,
        )

        rmse = root_mean_squared_error(
            self.y_test,
            self.predictions,
            
        )

        r2 = r2_score(
            self.y_test,
            self.predictions,
        )

        train_r2 = r2_score(
            self.y_train,
            self.train_predictions,
        )

        test_r2 = r2_score(
            self.y_test,
            self.predictions,
        )

        print("\n" + "=" * 60)
        print("MODEL EVALUATION")
        print("=" * 60)

        print(f"MAE  : {mae:.6f}")
        print(f"RMSE : {rmse:.6f}")
        print(f"R²   : {r2:.6f}")
        print(f"train_R²   : {train_r2:.6f}")
        print(f"test_R²   : {test_r2:.6f}")


    def run(self):

        self.load_model_outputs()
        self.evaluate()

def main():

    evaluator = ModelEvaluator()
    evaluator.run()

if __name__ == "__main__":
    main()

