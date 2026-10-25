from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Capstone API is running successfully!"}

@app.get("/predict/{country}")
def predict_country(country: str):
    """Gets predictions for a specific country or all countries combined."""
    if country.lower() == "all":
        return {"scope": "all countries combined", "prediction": "Aggregated results"}
    return {"scope": country, "prediction": f"Results for {country}"}
