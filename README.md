# StyleCast Closet AI

Backend recommendation system for building outfits and suggesting clothing combinations.

## Overview

This project implements a modular FastAPI backend that allows users to:

* browse available clothing products
* build outfits from selected items
* detect missing outfit categories
* receive recommendations to complete an outfit
* get similar product suggestions

The focus of the project is backend architecture, API design, and recommendation logic.

---

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
* JSON dataset

---

## Project Structure

```
stylecast-closet-ai/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── recommender.py
│   ├── schemas.py
│   └── data_loader.py
│
├── data/
│   └── products.json
│
├── README.md
├── architecture.md
├── requirements.txt
└── .gitignore
```

---

# How to Run the Project Locally

## 1. Clone the repository

```
git clone https://github.com/RehanChanegaon/stylecast-closet-ai.git
cd stylecast-closet-ai
```

---

## 2. Create a virtual environment

Windows (PowerShell):

```
python -m venv venv
```

Activate it:

```
.\venv\Scripts\activate
```

Your terminal should now show something like:

```
(venv) PS C:\...\stylecast-closet-ai>
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Run the API server

```
uvicorn app.main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
Application startup complete
```

---

## 5. Open the API documentation

Open this in your browser:

```
http://127.0.0.1:8000/docs
```

FastAPI automatically generates an interactive Swagger UI where all endpoints can be tested.

---

# API Endpoints

## Health Check

```
GET /
```

Example response:

```json
{
  "message": "StyleCast Closet AI API is running"
}
```

---

## Get All Products

```
GET /products
```

Returns all available products from the dataset.

---

## Build Outfit

```
POST /outfit
```

Example request:

```json
{
  "items": ["top_001", "bottom_001"]
}
```

The API returns:

* selected outfit items
* missing outfit categories
* recommended items to complete the outfit

---

## Get Outfit Recommendations

```
GET /recommendations/outfit
```

Example:

```
/recommendations/outfit?items=top_001,bottom_001
```

Returns recommended items to complete the outfit.

---

## Get Similar Products

```
GET /recommendations/similar/{product_id}
```

Example:

```
/recommendations/similar/top_001
```

Returns similar products based on category, color, and style tags.

---

# Recommendation Logic

The recommendation system uses a rule-based scoring approach.

### Outfit Completion

The system:

* checks which clothing categories are already selected
* determines missing categories
* finds candidate items to complete the outfit
* ranks them based on:

  * category compatibility
  * color compatibility
  * overlapping style tags

---

### Similar Product Recommendations

Products are ranked based on:

* same category
* matching colors
* overlapping style tags

---

# Design Approach

A rule-based approach was used because:

* the dataset is small
* the relationships are easy to interpret
* deterministic scoring is easier to validate
* it keeps the system simple and explainable

---

# Possible Improvements

Future improvements could include:

* database integration (PostgreSQL / MongoDB)
* user accounts and saved outfits
* caching frequently requested recommendations
* machine learning–based recommendations
* Docker containerization
* cloud deployment

---

# Author

Rehan Chanegaon
Master of Data Science & Analytics
University of Calgary
