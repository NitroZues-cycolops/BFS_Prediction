# BFS Prediction

A Black Friday purchase amount predictor with a FastAPI backend (serving a trained
scikit-learn model) and a Streamlit frontend for user input.

## Project Structure

BFS_Prediction/
├── backend/ # FastAPI app + ML model
│ ├── app.py
│ ├── model/
│ ├── Schema/
│ ├── dockerfile
│ └── requirements_api.txt
├── frontend/ # Streamlit UI
│ ├── frontend.py
│ ├── dockerfile
│ └── requirements_stream.txt
└── docker-compose.yml


## Running the App

**Requirements:** Docker and Docker Compose installed.

```bash
docker compose up --build
```

Once running:
- **Streamlit UI:** http://localhost:8501
- **FastAPI docs (Swagger UI):** http://localhost:5000/docs

To stop:
```bash
Ctrl+C
docker compose down
```

## What It Does

Enter customer details (gender, age, occupation, city category, product
categories, etc.) in the Streamlit form, and the app predicts the expected
purchase amount using a trained scikit-learn pipeline (RandomForest) served
via FastAPI.

## Tech Stack
- **Backend:** FastAPI, scikit-learn, pandas, Pydantic
- **Frontend:** Streamlit
- **Model:** RandomForest (trained on Black Friday sales dataset)
- **Containerization:** Docker, Docker Compose

## Known Limitations / TODO

The biggest problem is that model R2 score is not good
R²: 0.623895822100649
3050.495748200247
In the future commits focus would be on increasing the accuracy of the model upto a benchmark of 90 percent and using a proper frontend. Might be Vim or react
