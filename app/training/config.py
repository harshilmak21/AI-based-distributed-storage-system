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