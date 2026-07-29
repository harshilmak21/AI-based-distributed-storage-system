import random
from node import StorageNode
from config import NODE_PROFILES



def generate_node(node_number : int) -> StorageNode:

# "latency": (10, 40),
# "bandwidth": (400, 800),
# "reliability": (96, 99),
# "failure_rate": (1, 4),
# "current_load": (20, 60),

        
    profile_name = random.choice(list(NODE_PROFILES.keys()))
    profile = NODE_PROFILES[profile_name]
    #   * -- unpacking operator
    free_storage = random.uniform(*profile["free_storage"])
    cpu_usage = random.uniform(*profile["cpu_usage"])
    memory_usage = random.uniform(*profile["memory_usage"])
    latency = random.uniform(*profile["latency"])
    bandwidth = random.uniform(*profile["bandwidth"])
    reliability = random.uniform(*profile["reliability"])
    failure_rate = random.uniform(*profile["failure_rate"])
    current_load = random.uniform(*profile["current_load"])

    return StorageNode(
        node_id = f"Node_{node_number}",
        free_storage=free_storage,
        cpu_usage=cpu_usage,
        memory_usage=memory_usage,
        latency=latency,
        bandwidth=bandwidth,
        reliability=reliability,
        failure_rate=failure_rate,
        current_load=current_load,
    )

def generate_cluster(num_nodes:int) ->list[StorageNode]:
    cluster = []
    for i in range(1,num_nodes + 1):
        cluster.append(generate_node(i))
    return cluster

