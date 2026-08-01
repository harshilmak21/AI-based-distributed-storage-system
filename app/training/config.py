from pathlib import Path


TRAINING_DIR = Path(__file__).resolve().parent
APP_DIR = TRAINING_DIR.parent
PROJECT_ROOT = APP_DIR.parent

DATASET_PATH = (
    Path(__file__).resolve()
    .parent.parent
    / "datasets"
    / "training_dataset.csv"
)

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

EDA_DIR = ARTIFACTS_DIR / "eda"

MODEL_DIR = ARTIFACTS_DIR / "models"

REPORT_DIR = ARTIFACTS_DIR / "reports"

METRICS_DIR = ARTIFACTS_DIR / "metrics"

TARGET_COLUMN = "expert_score"

FEATURE_COLUMNS = [
    "free_storage",
    "cpu_usage",
    "memory_usage",
    "latency",
    "bandwidth",
    "reliability",
    "failure_rate",
    "current_load",
]

DROP_COLUMNS = [
    "cluster_id",
    "node_id",
    "rank",
]

TEST_SIZE = 0.20

RANDOM_STATE = 42

# Random FOrest Configuration

N_ESTIMATORS = 200

MAX_DEPTH = None

MIN_SAMPLES_SPLIT = 2

MIN_SAMPLES_LEAF = 1

N_JOBS = -1