from app.simulator.node import StorageNode
from app.simulator.scoring import calculate_score


def main():

    node = StorageNode(
        
        node_id="Test",
        free_storage=850,
        cpu_usage=90,
        memory_usage=25,
        latency=10,
        bandwidth=900,
        reliability=99.5,
        failure_rate=0.3,
        current_load=18,
    )

    expert_score = calculate_score(node)

    print(f"Expert Score: {expert_score:.6f}")


if __name__ == "__main__":
    main()