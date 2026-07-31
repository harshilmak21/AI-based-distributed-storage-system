from pathlib import Path
from data_loader import load_dataset
import pandas as pd

class EDAAnalyzer:

    def __init__(self):
        self.df = load_dataset

    def run(self):
        print("Running Shit")

def main():
    analyzer = EDAAnalyzer()
    analyzer.run()

if __name__ == "__main__":
    main()