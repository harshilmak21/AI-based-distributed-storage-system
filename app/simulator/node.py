from dataclasses import dataclass

@dataclass
class StorageNode:
    node_id : str
    free_storage : float
    cpu_usage : float
    memory_usage : float

    latency : float
    bandwidth : float

    reliability : float
    failure_rate: float

    current_load : float