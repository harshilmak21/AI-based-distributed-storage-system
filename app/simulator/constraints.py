from app.simulator.config import NODE_CONSTRAINTS
from app.simulator.node import StorageNode

def is_node_eligible(node: StorageNode) -> bool:

    if node.free_storage < NODE_CONSTRAINTS["min_free_storage"]:
        return False

    if node.cpu_usage > NODE_CONSTRAINTS["max_cpu_usage"]:
        return False

    if node.memory_usage > NODE_CONSTRAINTS["max_memory_usage"]:
        return False

    if node.current_load > NODE_CONSTRAINTS["max_current_load"]:
        return False

    if node.failure_rate > NODE_CONSTRAINTS["max_failure_rate"]:
        return False

    return True
