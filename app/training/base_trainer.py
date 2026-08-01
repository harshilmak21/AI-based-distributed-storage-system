from abc import ABC,abstractmethod
from preprocess import DataPreprocessor
from training_results import TrainingResult

class BaseTrainer(ABC):

    def __init__(self):

        self.model = None

        self.X_train = None
        self.X_test = None

        self.y_train = None
        self.y_test = None

        self.predictions = None

    def load_data(self):
        """
        Load preprocessed dataset.
        """

        preprocessor = DataPreprocessor()

        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        ) = preprocessor.run()

    @abstractmethod
    def build_model(self):
        pass
    def train(self):
        self.model.fit(
            self.X_train,
            self.y_train,
        )

    def predict(self):
        print("\n Generating Prediction!!")

        self.train_predictions = self.model.predict(
            self.X_train
        )
        self.predictions = self.model.predict(self.X_test)
        print("predcitions completedd.")

    def run(self):

        self.load_data()

        self.build_model()

        self.train()

        self.predict()

        return TrainingResult(
            self.model,
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
            self.train_predictions,
            self.predictions,
        )