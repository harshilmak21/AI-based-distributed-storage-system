from app.simulator.config import FEATURE_WEIGHTS
from app.simulator.config import  NODE_PROFILES
from app.simulator.config import FEATURE_RANGES

from app.simulator.node import StorageNode

def normalize(
    value : float,
    minimum : float , 
    maximum : float

) -> float:
    return (value - minimum) / (maximum - minimum)

def inverse_normalize(
        value : float,
        minimum : float,
        maximum : float
) -> float : 
    return 1 - ((value - minimum) / (maximum - minimum))



def calculate_score(node : StorageNode) -> float:
    

    storage_score = normalize(
        node.free_storage,
        *FEATURE_RANGES["free_storage"]
    )
    cpu_score = normalize(
        node.cpu_usage,
        *FEATURE_RANGES["cpu_usage"]
    )
    
    memory_score = normalize(
        node.memory_usage,
        *FEATURE_RANGES["memory_usage"]
    )
    
    latency_score = normalize(
        node.latency,
        *FEATURE_RANGES["latency"]
    )
    
    bandwidth_score = normalize(
        node.bandwidth,
        *FEATURE_RANGES["bandwidth"]
    )
    
    reliability_score = normalize(
        node.reliability,
        *FEATURE_RANGES["reliability"]
    )
    
    failure_score = normalize(
        node.failure_rate,
        *FEATURE_RANGES["failure_rate"]
    )
    
    current_load_score = normalize(
        node.current_load,
        *FEATURE_RANGES["current_load"]
    )

    score = 0.0

    score += storage_score * FEATURE_WEIGHTS["free_storage"]
    score += cpu_score * FEATURE_WEIGHTS["cpu_usage"]
    score += memory_score * FEATURE_WEIGHTS["memory_usage"]
    score += latency_score * FEATURE_WEIGHTS["latency"]
    score += bandwidth_score * FEATURE_WEIGHTS["bandwidth"]
    score += reliability_score * FEATURE_WEIGHTS["reliability"]
    score += failure_score * FEATURE_WEIGHTS["failure_rate"]
    score += current_load_score * FEATURE_WEIGHTS["current_load"]

    return score

# FEATURE_RANGES = {
#     "free_storage": (100, 1000),
#     "cpu_usage": (5, 95),
#     "memory_usage": (10, 90),
#     "latency": (5, 80),
#     "bandwidth": (400, 1000),
#     "reliability": (95, 100),
#     "failure_rate": (0, 5),
#     "current_load": (5, 95),
# }

# FEATURE_WEIGHTS = {
#     "free_storage": 0.25,
#     "cpu_usage": 0.20,
#     "memory_usage": 0.10,
#     "latency": 0.15,
#     "bandwidth": 0.10,
#     "reliability": 0.10,
#     "failure_rate": 0.05,
#     "current_load": 0.05,
# }TS["free_storage"] + cpu_score * FEATURE_WEIGHTS["cpu_usage"]

# FEATURE_RANGES = {
#     "free_storage": (100, 1000),
#     "cpu_usage": (5, 95),
#     "memory_usage": (10, 90),
#     "latency": (5, 80),
#     "bandwidth": (400, 1000),
#     "reliability": (95, 100),
#     "failure_rate": (0, 5),
#     "current_load": (5, 95),
# }

# FEATURE_WEIGHTS = {
#     "free_storage": 0.25,
#     "cpu_usage": 0.20,
#     "memory_usage": 0.10,
#     "latency": 0.15,
#     "bandwidth": 0.10,
#     "reliability": 0.10,
#     "failure_rate": 0.05,
#     "current_load": 0.05,
# }