from fastapi import APIRouter, HTTPException, status
from app.schemas import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])

db_items = {}
id_counter = 1

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    global id_counter
    new_item = {"id": id_counter, **item.model_dump()}
    db_items[id_counter] = new_item
    id_counter += 1
    return new_item

@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    if item_id not in db_items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item não encontrado"
        )
    return db_items[item_id]