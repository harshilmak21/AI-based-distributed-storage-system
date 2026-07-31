from app.simulator.cluster import generate_cluster
from app.simulator.ranking import rank_nodes

cluster = generate_cluster(20)

ranked_nodes = rank_nodes(cluster)

for rank,ranked_node in enumerate(ranked_nodes , start=1):
    print(
        f"{rank}."
        f"{ranked_node.node.node_id} "
        f"Score = {ranked_node.score:.3f}"
    )