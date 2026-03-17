from pydantic import BaseModel, ConfigDict


class BrandOut(BaseModel):
    id: int
    name: str
    discount_percentage: float

    model_config = ConfigDict(from_attributes=True)
