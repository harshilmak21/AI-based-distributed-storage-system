from ranking import RanKedNode

def ranked_node_to_dict(
        cluster_id : int,
        ranked_node : RanKedNode,
        rank:int
) -> dict :

    node = ranked_node.node

    return {
        "cluster_id": cluster_id,
        "node_id": node.node_id,

        "free_storage": node.free_storage,
        "cpu_usage": node.cpu_usage,
        "memory_usage": node.memory_usage,

        "latency": node.latency,
        "bandwidth": node.bandwidth,

        "reliability": node.reliability,
        "failure_rate": node.failure_rate,

        "current_load": node.current_load,

        "expert_score": ranked_node.score,
        "rank": rank
    }

from cluster import generate_cluster
from ranking import rank_nodes

def generate_cluster_rows(
        cluster_id : int ,
        num_nodes : int

) -> list[dict]:
    rows = []

    cluster = generate_cluster(num_nodes)
    ranked_nodes = rank_nodes(cluster)

    for rank,ranked_node in enumerate(ranked_nodes , start = 1):

        rows.append(
            ranked_node_to_dict(
                cluster_id,
                ranked_node,
                rank
            )
        )
    return rows

def generate_dataset(
        num_clusters : int,
        nodes_per_cluster : int
) -> list[dict] :

    dataset = []

    for cluster_id in range(1,num_clusters + 1):

        rows = generate_cluster_rows(
            cluster_id,
            nodes_per_cluster
        )

        dataset.extend(rows)

    return dataset

import pandas as pd

def save_dataset(
        rows : list[dict],
        filename : str = "training_dataset.csv"
):

    df = pd.DataFrame(rows)

    df.to_csv(
        filename,
        index = False
    )
    print(f"Saved {len(df)} rows to {filename}")


if __name__ == "__main__":
    print("Starting dataset generation...")

    rows = generate_dataset(
        num_clusters=100,
        nodes_per_cluster=10
    )

    print(f"Generated {len(rows)} rows")

    save_dataset(rows)

    print("Done!")