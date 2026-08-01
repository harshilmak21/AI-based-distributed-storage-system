from sklearn.model_selection import train_test_split

from config import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    TEST_SIZE,RANDOM_STATE
)

from data_loader import load_dataset

class DataPreprocessor:

    def __init__(self):
        self.df = None

        self.X = None
        self.y = None

        self.X_train = None
        self.X_test = None

        self.y_train = None
        self.y_test = None

    def load_data(self) -> None:

        print("Loading Dataset!!")

        self.df = load_dataset()
        print("Dataset loaded Successfully!!!.")

    def prepare_features(self) -> None:

        print("\nPreparing features..")

        self.X = self.df[FEATURE_COLUMNS]
        self.y = self.df[TARGET_COLUMN]

        print(f"Features : {self.X.shape}")
        print(f"target : {self.y.shape}")

    def split_dataset(self) -> None:

        print("\n Spliting Datset..")

        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=TEST_SIZE,random_state=RANDOM_STATE,shuffle=True)

        print(f"Training Samples : {len(self.X_train)}")
        print(f"Testing Samples  : {len(self.X_test)}")

    def preprocess(self):

        return (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test
        )

    def run(self):

        self.load_data()
        self.prepare_features()
        self.split_dataset()

        return self.preprocess()

def main():

    preprocessor = DataPreprocessor()
    preprocessor.run()

if __name__ == "__main__":
    main()