from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, example="Notebook")
    description: str | None = Field(default=None, example="Notebook para desenvolvimento")
    price: float = Field(..., gt=0, example=3500.00)

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True