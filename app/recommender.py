from fastapi import HTTPException
from typing import Dict, List, Set

from app.data_loader import load_products

REQUIRED_OUTFIT_CATEGORIES = ["top", "bottom", "shoes", "outerwear", "accessories"]

CATEGORY_COMPATIBILITY = {
    "top": {"bottom", "shoes", "outerwear", "accessories"},
    "bottom": {"top", "shoes", "outerwear", "accessories"},
    "shoes": {"top", "bottom", "outerwear", "accessories"},
    "outerwear": {"top", "bottom", "shoes", "accessories"},
    "accessories": {"top", "bottom", "shoes", "outerwear"},
}

NEUTRAL_COLORS = {"white", "black", "grey", "gray", "beige", "cream", "navy"}

COLOR_COMPATIBILITY = {
    "white": {"black", "blue", "grey", "gray", "beige", "cream", "navy", "white"},
    "black": {"white", "blue", "grey", "gray", "beige", "cream", "navy", "black"},
    "blue": {"white", "black", "grey", "gray", "beige", "cream", "navy"},
    "grey": {"white", "black", "blue", "beige", "cream", "navy", "grey"},
    "gray": {"white", "black", "blue", "beige", "cream", "navy", "gray"},
    "beige": {"white", "black", "blue", "grey", "gray", "cream", "navy", "beige"},
    "cream": {"white", "black", "blue", "grey", "gray", "beige", "navy", "cream"},
    "navy": {"white", "black", "beige", "cream", "grey", "gray", "blue", "navy"},
}

PRODUCTS = load_products()
PRODUCT_MAP = {product["product_id"]: product for product in PRODUCTS}


def get_all_products() -> List[Dict]:
    return PRODUCTS


def get_product(product_id: str) -> Dict:
    product = PRODUCT_MAP.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return product


def normalize_color(color: str) -> str:
    return color.strip().lower()


def tags_set(product: Dict) -> Set[str]:
    return {tag.strip().lower() for tag in product.get("style_tags", [])}


def color_match_score(color1: str, color2: str) -> int:
    c1, c2 = normalize_color(color1), normalize_color(color2)

    if c1 == c2:
        return 3

    if c1 in NEUTRAL_COLORS or c2 in NEUTRAL_COLORS:
        return 2

    if c2 in COLOR_COMPATIBILITY.get(c1, set()):
        return 2

    return 0


def tag_overlap_score(product1: Dict, product2: Dict) -> int:
    overlap = tags_set(product1) & tags_set(product2)
    return len(overlap) * 2


def category_match_score(product1: Dict, product2: Dict) -> int:
    c1 = product1["category"]
    c2 = product2["category"]

    if c1 == c2:
        return 4

    if c2 in CATEGORY_COMPATIBILITY.get(c1, set()):
        return 2

    return 0


def similarity_score(base_product: Dict, candidate: Dict) -> int:
    if base_product["product_id"] == candidate["product_id"]:
        return -1

    score = 0

    if base_product["category"] == candidate["category"]:
        score += 5

    score += color_match_score(base_product["color"], candidate["color"])
    score += tag_overlap_score(base_product, candidate)

    return score


def compatibility_score(selected_items: List[Dict], candidate: Dict) -> int:
    selected_ids = {item["product_id"] for item in selected_items}
    selected_categories = {item["category"] for item in selected_items}

    if candidate["product_id"] in selected_ids:
        return -1

    score = 0

    if candidate["category"] in selected_categories:
        score -= 3

    for item in selected_items:
        score += category_match_score(item, candidate)
        score += color_match_score(item["color"], candidate["color"])
        score += tag_overlap_score(item, candidate)

    return score


def get_missing_categories(selected_items: List[Dict]) -> List[str]:
    present_categories = {item["category"] for item in selected_items}
    return [category for category in REQUIRED_OUTFIT_CATEGORIES if category not in present_categories]


def recommend_outfit_items(selected_items: List[Dict], limit: int = 5) -> List[Dict]:
    missing_categories = set(get_missing_categories(selected_items))
    selected_ids = {item["product_id"] for item in selected_items}
    candidates = []

    for product in PRODUCTS:
        if product["product_id"] in selected_ids:
            continue

        score = compatibility_score(selected_items, product)

        if product["category"] in missing_categories:
            score += 5

        if score > 0:
            candidates.append({
                "product_id": product["product_id"],
                "brand": product["brand"],
                "name": product["name"],
                "category": product["category"],
                "color": product["color"],
                "price": product["price"],
                "score": score
            })

    candidates.sort(key=lambda x: (-x["score"], x["price"]))
    return candidates[:limit]


def recommend_similar_items(product_id: str, limit: int = 5) -> List[Dict]:
    base_product = get_product(product_id)
    candidates = []

    for product in PRODUCTS:
        score = similarity_score(base_product, product)

        if score > 0:
            candidates.append({
                "product_id": product["product_id"],
                "brand": product["brand"],
                "name": product["name"],
                "category": product["category"],
                "color": product["color"],
                "price": product["price"],
                "score": score
            })

    candidates.sort(key=lambda x: (-x["score"], x["price"]))
    return candidates[:limit]