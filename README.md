# StyleCast Closet AI

A backend system for an AI-powered outfit builder that allows users to:
- select products
- build outfits
- receive outfit completion recommendations
- receive similar product suggestions

## Features

- Product listing API
- Outfit builder API
- Missing category detection
- Outfit completion recommendations
- Similar product recommendations
- Swagger/OpenAPI documentation via FastAPI

## Tech Stack

- Python
- FastAPI
- Pydantic
- JSON dataset

## Project Structure

```text
stylecast-ai/
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── recommender.py
│   ├── schemas.py
│   └── data_loader.py
├── data/
│   └── products.json
├── README.md
├── architecture.md
├── requirements.txt
└── .gitignore