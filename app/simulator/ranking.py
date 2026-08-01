from dataclasses import dataclass
from node import StorageNode
from constraints import is_node_eligible
from scoring import calculate_score

@dataclass
class RanKedNode:
    node : StorageNode
    score : float

def rank_nodes(cluster : list[StorageNode]) -> list[RanKedNode]:

    ranked_nodes = []

    for node in cluster:

        if not is_node_eligible(node):
            continue

        score = calculate_score(node)

        ranked_node = RanKedNode(
            node = node,
            score = score
        )

        ranked_nodes.append(ranked_node)

        ranked_nodes.sort(
            key=lambda ranked_node : ranked_node.score,
            reverse = True
        )

    return ranked_nodes