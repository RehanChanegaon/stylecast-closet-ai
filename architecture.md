
---

# 3. `architecture.md`

Paste this:

```md
# Architecture Overview

## High-Level Design

The application is divided into four logical layers:

### 1. API Layer
Implemented using FastAPI.

Responsibilities:
- expose REST endpoints
- receive and validate requests
- return JSON responses

File:
- `app/routes.py`

### 2. Schema Layer
Implemented using Pydantic models.

Responsibilities:
- validate input request bodies
- enforce API request structure

File:
- `app/schemas.py`

### 3. Recommendation Layer
Contains the core business logic.

Responsibilities:
- retrieve products
- identify missing outfit categories
- generate outfit completion recommendations
- generate similar product recommendations
- rank candidate items

File:
- `app/recommender.py`

### 4. Data Layer
Loads product data from a JSON dataset.

Responsibilities:
- read product catalog
- return structured product data

File:
- `app/data_loader.py`

---

## Request Flow

1. A client sends an HTTP request to the FastAPI server
2. The route receives the request
3. Pydantic validates input if needed
4. The route calls the recommender layer
5. The recommender loads and evaluates product data
6. The ranked result is returned as JSON

---

## Key Files

### `main.py`
Creates the FastAPI app instance and registers routes.

### `routes.py`
Defines all available API endpoints.

### `schemas.py`
Defines request validation models.

### `recommender.py`
Contains the recommendation algorithms and ranking logic.

### `data_loader.py`
Loads the product dataset from `data/products.json`.

---

## Recommendation Logic

### Outfit Completion
For a selected outfit, the system:
- extracts existing categories
- determines missing categories
- evaluates available candidate items
- boosts items that fill missing categories
- ranks them based on:
  - category compatibility
  - color match / neutral compatibility
  - overlapping style tags

### Similar Product Recommendations
For a given product, the system:
- compares it with all other products
- prioritizes items in the same category
- rewards matching colors
- rewards overlapping style tags
- sorts by descending score

---

## Why a Rule-Based Approach

A rule-based approach was selected because:
- the dataset is small
- the relationships are interpretable
- the implementation is deterministic
- it is easier to explain during evaluation

This also makes the solution suitable for an assignment environment where clarity and reasoning are more important than model complexity.

---

## Scalability Considerations

If the system were extended for production, the following improvements would be recommended:

- replace JSON with a database
- add product/category/style tag normalization tables
- cache frequent recommendation queries
- add outfit persistence
- support user personalization
- upgrade recommendation logic using embeddings or ML ranking

---

## Proposed Database Schema

### `products`
- `product_id` (PK)
- `brand`
- `name`
- `category`
- `price`
- `color`
- `image_url`

### `style_tags`
- `tag_id` (PK)
- `tag_name`

### `product_style_tags`
- `product_id` (FK)
- `tag_id` (FK)

### `outfits` (optional)
- `outfit_id` (PK)
- `created_at`

### `outfit_items` (optional)
- `outfit_id` (FK)
- `product_id` (FK)

---

## Summary

This architecture separates API handling, validation, business logic, and data access. That makes the codebase:
- modular
- readable
- easy to test
- easy to extend
