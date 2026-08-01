from random_forest_trainer import RandomForestTrainer
from model_registry import ModelRegistry


def main():

    trainer = RandomForestTrainer()

    result = trainer.run()

    registry = ModelRegistry()

    registry.save_model(result)

    loaded_model = registry.load_model()

    print(type(loaded_model))

if __name__ == "__main__":
    main()