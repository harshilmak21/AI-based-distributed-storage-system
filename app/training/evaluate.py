from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score,
)

from random_forest_trainer import RandomForestTrainer
from training_results import TrainingResult

class ModelEvaluator:
    """
    Evaluate a trained regression model.
    """

    def __init__(self, training_result : TrainingResult) :
        self.result = training_result


    def evaluate(self):


        mae = mean_absolute_error(
            self.result.y_test,
            self.result.test_predictions,
        )

        rmse = root_mean_squared_error(
            self.result.y_test,
            self.result.test_predictions,
        )

        test_r2 = r2_score(
            self.result.y_test,
            self.result.test_predictions,
        )

        train_r2 = r2_score(
            self.result.y_train,
            self.result.train_predictions,
        )

        print("\n" + "=" * 60)
        print("MODEL EVALUATION")
        print("=" * 60)

        print(f"MAE        : {mae:.6f}")
        print(f"RMSE       : {rmse:.6f}")
        print(f"Train R²   : {train_r2:.6f}")
        print(f"Test R²    : {test_r2:.6f}")
        print(f"Gap        : {abs(train_r2-test_r2):.6f}")

    def run(self):

        self.evaluate()


def main():

    trainer = RandomForestTrainer()
    TrainingResult = trainer.run()
    evaluator = ModelEvaluator(TrainingResult)
    evaluator.evaluate()


if __name__ == "__main__":
    main()  