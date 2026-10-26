import asyncio
import httpx

from app.inference.predictor import Predictor
from app.training.config import FEATURE_COLUMNS

NODE_URLS = {
    f"node-{i}" : f"http://localhost:{8000 + i}/metrics"
    for i in range(1 , 6)
}

class NodeCoordinator:

    def __init__(self) : 

        self.predictor = Predictor()

    async def _get_node_score(self , client ,node_id , url):
        try:
            response = await client.get(url)
            response.raise_for_status()
            metrics = response.json()


            features = {
                column : metrics[column]
                for column in FEATURE_COLUMNS
            }

            score = self.predictor.predict(features)
            return {
                "node_id" : node_id,
                "expert_score": score ,
                "metrics": features,
                "status" : "available",
            }


        except (httpx.HTTPError,KeyError,ValueError) as exc:
            return {
                "node_id" : node_id ,
                "status" : "unavailbbale",
                "error" : str(exc),
            }

    async def rank_nodes(self) :

        async with httpx.AsyncClient(timeout=5.0) as client:
            results = await asyncio.gather(
                *[
                    self._get_node_score(client, node_id, url)
                    for node_id, url in NODE_URLS.items()
                ]

            )
        available = [
            result for result in results
            if result["status"] == "available"
        ]
        unavailable = [
            result for result in results
            if result["status"] == "unavailable"
        ]


        available.sort(
            key = lambda result : result["expert_score"],
            reverse = True,
        )

        for rank , result in enumerate(available , start = 1):
            result["rank"] = rank

        return {
            "ranked_nodes": available,
            "unavailable_nodes": unavailable,
            }

