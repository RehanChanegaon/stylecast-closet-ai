# StyleCast Closet AI

Backend recommendation system for an AI-powered outfit builder.

## Overview

This project implements a modular FastAPI backend for a fashion outfit recommendation system. It allows users to:

- browse available products
- build outfits by selecting clothing items
- identify missing outfit categories
- receive recommendations to complete an outfit
- receive similar product recommendations

The system is designed as a backend-focused assignment, with an emphasis on:

- API design
- recommendation logic
- modular architecture
- scalability considerations

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- JSON dataset

## Project Structure

```text
stylecast-closet-ai/
├── app/
│   ├── __init__.py
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
