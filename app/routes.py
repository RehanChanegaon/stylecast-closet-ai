from fastapi import APIRouter

from app.schemas import OutfitRequest
from app.recommender import (
    get_all_products,
    get_product,
    get_missing_categories,
    recommend_outfit_items,
    recommend_similar_items,
)

router = APIRouter()


@router.get("/")
def root():
    return {"message": "StyleCast Closet AI API is running"}


@router.get("/products")
def list_products():
    return get_all_products()


@router.post("/outfit")
def create_or_update_outfit(request: OutfitRequest):
    selected_items = [get_product(product_id) for product_id in request.items]
    missing_categories = get_missing_categories(selected_items)
    recommended_items = recommend_outfit_items(selected_items)

    return {
        "current_items": selected_items,
        "missing_categories": missing_categories,
        "recommended_items": recommended_items
    }


@router.get("/recommendations/outfit")
def get_outfit_recommendations(items: str):
    item_ids = [item.strip() for item in items.split(",") if item.strip()]
    selected_items = [get_product(product_id) for product_id in item_ids]
    missing_categories = get_missing_categories(selected_items)
    recommended_items = recommend_outfit_items(selected_items)

    return {
        "current_items": selected_items,
        "missing_categories": missing_categories,
        "recommended_items": recommended_items
    }


@router.get("/recommendations/similar/{product_id}")
def get_similar_products(product_id: str):
    base_product = get_product(product_id)
    similar_items = recommend_similar_items(product_id)

    return {
        "selected_product": base_product,
        "similar_items": similar_items
    }