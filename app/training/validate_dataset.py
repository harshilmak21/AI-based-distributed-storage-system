import pandas as pd
from pathlib import Path

from pandas.api.types import (
    is_integer_dtype,
    is_float_dtype,
    is_numeric_dtype
)

from config import DATASET_PATH
EXPECTED_COLUMNS = [
    "cluster_id",
    "node_id",
    "free_storage",
    "cpu_usage",
    "memory_usage",
    "latency",
    "bandwidth",
    "reliability",
    "failure_rate",
    "current_load",
    "expert_score",
    "rank",
]

EXPECTED_DTYPES = {
    "cluster_id": "int",
    "node_id": "int",
    "free_storage": "numeric",
    "cpu_usage": "numeric",
    "memory_usage": "numeric",
    "latency": "numeric",
    "bandwidth": "numeric",
    "reliability": "numeric",
    "failure_rate": "numeric",
    "current_load": "numeric",
    "expert_score": "numeric",
    "rank": "int",
}

from data_loader import load_dataset



def print_summary(df : pd.DataFrame) -> None:

    print("=" * 50)
    print("DATASET SUMMARY")
    print("=" * 50)

    print(f"\nShape : {df.shape}")

    print(f"\nColumns : {df.columns.tolist()}")

    print(f"\nData Types : {df.dtypes}")

    print(f"\nFirst 5 Rows: {df.head}")

def validate_columns(df : pd.DataFrame) -> bool :

    print("\n" + "=" * 50)
    print("COLUMN VALIDATION")
    print("=" * 50)

    actual_columns = set(df.columns)
    expected_columns = set(EXPECTED_COLUMNS)

    missing_columns = expected_columns - actual_columns
    extra_columns = actual_columns - expected_columns

    if missing_columns:
        print("Missing_columns:")
        for column in sorted(missing_columns):
            print(f"-> {column}")

    if extra_columns:
        print("Unexpected Columns:")
        for column in sorted(extra_columns):
            print

    if not missing_columns and not  extra_columns:
        print(f"ALl required COlumns presetn!!")
        return True

def validate_data_types(df : pd.DataFrame) -> bool :
    print("\n" + "=" * 50)
    print("DATA TYPE VALIDATION")
    print("=" * 50)

    passed = True

    for column,expected_type in EXPECTED_DTYPES.items():

        if expected_type == "int":
            valid = is_integer_dtype(df[column])

        elif expected_type == "numeric":
            valid = is_numeric_dtype(df[column])

        else:
            valid = False

        if valid:
            print(f"{column :<20} {df[column].dtype}")

        else :
            print(
                f" {column :<20} Expected {expected_type},"
                f"Found {df[column].dtype}"
            )
            passed = False
    return passed


def validate_missing_values(df : pd.DataFrame) -> bool:
    missing_counts = df.isna().sum()
    total_missing = missing_counts.sum()

    if total_missing == 0:
        print(f"No missing Values Found.!!")
        return True
    
    print(f"Total missing values : {total_missing}")

    for column , count in missing_counts.items():
        if count > 0:
            print(f"{column:<20} {count}")
    return False

def validate_duplicates(df : pd.DataFrame) -> bool :
    print("\n" + "=" * 50)
    print("DUPLICATE VALIDATION")
    print("=" * 50)

    duplicate_count = df.duplicated().sum()

    if duplicate_count == 0:
        print(f"No duplicates Found")
        return True

    else :
        print(f"Duplicate Rows Found : {duplicate_count}")
        return False


def validate_target(df : pd.DataFrame) -> bool :

    print("\n" + "=" * 50)
    print("TARGET VALIDATION")
    print("=" * 50)

    target = df["expert_score"]
    passed = True

    min_score = target.min()
    max_score = target.max()

    print(f"Minimum Score : {min_score:.2f}")
    print(f"Maximum Score : {max_score:.2f}")

    if min_score < 0 > max_score > 100:
        print("expert_score contains values outside the range [0-10]")
        passed = False
    else :
        print("Score range is valid")

    unique_scores = target.nunique()
    print(f"Unique Scores : {unique_scores}")

    if unique_scores <= 1:
        print("expert_score has no variation")
        passed = False

    else :
        print("Target Contains sufficient Variation")

    return passed


def validate_rank(df: pd.DataFrame) -> bool:
    print("\n" + "=" * 50)
    print("RANK VALIDATION")
    print("=" * 50)

    passed = True
    checked_clusters = 0
    failed_clusters = []

    for cluster_id, cluster_df in df.groupby("cluster_id"):

        checked_clusters += 1

        rank = cluster_df["rank"]

        expected_max_rank = len(cluster_df)

        min_rank = rank.min()
        max_rank = rank.max()

        duplicate_count = rank.duplicated().sum()

        expected_ranks = set(range(1, expected_max_rank + 1))
        actual_ranks = set(rank)

        missing_ranks = sorted(expected_ranks - actual_ranks)

        cluster_valid = (
            min_rank == 1
            and max_rank == expected_max_rank
            and duplicate_count == 0
            and len(missing_ranks) == 0
        )

        if not cluster_valid:

            passed = False

            failed_clusters.append(
                {
                    "cluster": cluster_id,
                    "min_rank": min_rank,
                    "max_rank": max_rank,
                    "expected_max": expected_max_rank,
                    "duplicates": duplicate_count,
                    "missing": missing_ranks,
                }
            )

    print(f"Clusters Checked : {checked_clusters}")

    if passed:
        print("All clusters have valid rankings.")
        return True

    print(f"Failed Clusters : {len(failed_clusters)}\n")

    for cluster in failed_clusters:

        print(f"Cluster {cluster['cluster']}")

        if cluster["min_rank"] != 1:
            print(f"Minimum rank is {cluster['min_rank']}")

        if cluster["max_rank"] != cluster["expected_max"]:
            print(
                f" Maximum rank should be "
                f"{cluster['expected_max']}, "
                f"found {cluster['max_rank']}"
            )

        if cluster["duplicates"] > 0:
            print(
                f" Duplicate ranks: "
                f"{cluster['duplicates']}"
            )

        if cluster["missing"]:
            print(
                f" Missing ranks: "
                f"{cluster['missing']}"
            )

        print()

    return False


def main():
    df = load_dataset()
    print_summary(df)
    validate_columns(df)
    validate_data_types(df)
    validate_missing_values(df)
    validate_duplicates(df)
    validate_target(df)
    validate_rank(df)

if __name__ == "__main__":
    main()