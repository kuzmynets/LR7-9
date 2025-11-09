import requests
from requests.exceptions import RequestException, Timeout
from src.external_api.models import CatFactModel, CatImageModel, CatCombinedModel

class CatService:
    fact_url: str = "https://catfact.ninja/fact"
    image_url: str = "https://api.thecatapi.com/v1/images/search"

    def get_cat_fact(self) -> CatFactModel:
        try:
            resp = requests.get(self.fact_url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            return CatFactModel(**data)
        except (RequestException, ValueError) as e:
            raise RuntimeError(f"Error fetching cat fact: {e}")

    def get_cat_image(self) -> CatImageModel:
        try:
            resp = requests.get(self.image_url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, list) or not data:
                raise RuntimeError("Invalid response for cat image")
            return CatImageModel(url=data[0]["url"])
        except (RequestException, ValueError, KeyError) as e:
            raise RuntimeError(f"Error fetching cat image: {e}")

    def get_cat_info(self) -> CatCombinedModel:
        fact = self.get_cat_fact()
        image = self.get_cat_image()
        return CatCombinedModel(fact=fact.fact, image_url=image.url)

service = CatService()
