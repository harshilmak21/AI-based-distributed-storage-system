from app.simulator.config import (
    FEATURE_RANGES,
    FEATURE_TYPES,
    FEATURE_WEIGHTS,
)
from app.simulator.node import StorageNode

def normalize(
    value: float,
    minimum: float,
    maximum: float,
) -> float:

    return (value - minimum) / (maximum - minimum)

def inverse_normalize(
    value: float,
    minimum: float,
    maximum: float,
) -> float:
    
    return 1 - normalize(value, minimum, maximum)


def calculate_score(node: StorageNode) -> float:
    
    score = 0.0

    for feature, weight in FEATURE_WEIGHTS.items():
        value = getattr(node, feature)
        minimum, maximum = FEATURE_RANGES[feature]
        feature_type = FEATURE_TYPES[feature]

        if feature_type == "benefit":
            normalized_value = normalize(
                value,
                minimum,
                maximum,
            )

        elif feature_type == "cost":
            normalized_value = inverse_normalize(
                value,
                minimum,
                maximum,
            )

        else:
            raise ValueError(
                f"Unknown feature type '{feature_type}' "
                f"for feature '{feature}'."
            )

        score += normalized_value * weight

    return score