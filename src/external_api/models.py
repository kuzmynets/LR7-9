from pydantic import BaseModel, Field, HttpUrl
from src.external_api.config import cat_config as cfg

class CatFactModel(BaseModel):
    fact: str = Field(..., min_length=cfg.min_fact_length, max_length=cfg.max_fact_length, description="Cat fact text")
    length: int = Field(..., ge=cfg.min_length_value, le=cfg.max_length_value, description="Length of fact")

    model_config = {"from_attributes": True}

class CatImageModel(BaseModel):
    url: HttpUrl = Field(..., min_length=cfg.min_url_length, max_length=cfg.max_url_length, description="Cat image URL")
    model_config = {"from_attributes": True}

class CatCombinedModel(BaseModel):
    fact: str = Field(..., min_length=cfg.min_fact_length, max_length=cfg.max_fact_length)
    image_url: HttpUrl = Field(..., min_length=cfg.min_url_length, max_length=cfg.max_url_length)
    model_config = {"from_attributes": True}
