from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data_loader import load_dataset
from config import EDA_DIR


class EDAAnalyzer:
    """
    Performs exploratory data analysis on the training dataset.
    """

    def __init__(self):
        self.df = load_dataset()

        EDA_DIR.mkdir(parents=True, exist_ok=True)

    def dataset_summary(self):
        """Print dataset summary."""

        print("\n" + "=" * 60)
        print("DATASET SUMMARY")
        print("=" * 60)

        rows, cols = self.df.shape

        print(f"Rows          : {rows}")
        print(f"Columns       : {cols}")

        memory = self.df.memory_usage(deep=True).sum() / 1024

        print(f"Memory Usage  : {memory:.2f} KB")

        print("\nColumns")

        for column in self.df.columns:
            print(f" - {column}")

    def descriptive_statistics(self):
        """Save descriptive statistics."""

        print("\nGenerating descriptive statistics...")

        stats = self.df.describe()

        stats.to_csv(EDA_DIR / "descriptive_statistics.csv")

        with open(EDA_DIR / "summary.txt", "w") as file:

            file.write("DATASET INFORMATION\n")
            file.write("=" * 60 + "\n\n")

            self.df.info(buf=file)

            file.write("\n\n")

            file.write("DESCRIPTIVE STATISTICS\n")
            file.write("=" * 60 + "\n")

            file.write(stats.to_string())

    def correlation_analysis(self):
        """Generate correlation heatmap."""

        print("Generating correlation heatmap...")

        corr = self.df.corr(numeric_only=True)

        plt.figure(figsize=(10, 8))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            linewidths=0.5,
        )

        plt.title("Feature Correlation Matrix")
        plt.tight_layout()

        plt.savefig(
            EDA_DIR / "correlation_heatmap.png",
            dpi=300,
        )

        plt.close()

        print("\nCorrelation with expert_score\n")

        target_corr = (
            corr["expert_score"]
            .sort_values(ascending=False)
        )

        print(target_corr)

        target_corr.to_csv(
            EDA_DIR / "target_correlations.csv"
        )

    def target_distribution(self):
        """Generate target histogram."""

        print("Generating target distribution...")

        plt.figure(figsize=(8, 5))

        sns.histplot(
            self.df["expert_score"],
            bins=20,
            kde=True,
        )

        plt.title("Expert Score Distribution")

        plt.xlabel("Expert Score")

        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig(
            EDA_DIR / "target_distribution.png",
            dpi=300,
        )

        plt.close()

    def run(self):

        self.dataset_summary()

        self.descriptive_statistics()

        self.correlation_analysis()

        self.target_distribution()

        print("\nEDA completed successfully.")

        print(f"\nArtifacts saved to:\n{EDA_DIR}")


def main():

    analyzer = EDAAnalyzer()

    analyzer.run()


if __name__ == "__main__":
    main()