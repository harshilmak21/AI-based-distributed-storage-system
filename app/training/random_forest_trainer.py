from sklearn.ensemble import RandomForestRegressor
from base_trainer import BaseTrainer

from config import (
    RANDOM_STATE,
    N_ESTIMATORS,
    MAX_DEPTH,
    MIN_SAMPLES_SPLIT,
    MIN_SAMPLES_LEAF,
    N_JOBS,
)

class RandomForestTrainer(BaseTrainer):

    def build_model(self):
         self.train_predictions = None
         self.model = RandomForestRegressor(
            n_estimators=N_ESTIMATORS,
            max_depth=MAX_DEPTH,
            min_samples_split=MIN_SAMPLES_SPLIT,
            min_samples_leaf=MIN_SAMPLES_LEAF,
            random_state=RANDOM_STATE,
            n_jobs=N_JOBS,
        )

         
def main():
     trainer = RandomForestTrainer()
     trainer.run()

if __name__ == "__main__":
     main()
