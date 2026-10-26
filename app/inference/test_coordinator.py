import asyncio
from app.inference.node_coordinator import NodeCoordinator

async def main():
    coordinator = NodeCoordinator()
    result = await coordinator.rank_nodes()


    print("Available Nodes")

    for node in result["ranked_nodes"]:
        print(
            f"Rank : {node['rank']} |"
            f"Node : {node['node_id']} |"
            f"Score : {node['expert_score']:.6f}"

        )

    if not result["unavailable_nodes"]:
        print("All storage nodes are available.")


if __name__ == "__main__":
    asyncio.run(main())