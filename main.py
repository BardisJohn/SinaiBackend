from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Render API")

# Επιτρέπουμε CORS ώστε το Flet app να μπορεί να κάνει requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ Η function σου — άλλαξέ την όπως θέλεις
def my_function(name: str) -> dict:
    result = f"Γεια σου, {name}! Η απάντηση από το Render είναι: {len(name) * 42}"
    return {"status": "ok", "result": result}


# ✅ Το endpoint που θα καλεί το Flet app
@app.get("/run")
def run_function(name: str = "World"):
    return my_function(name)


# Health check — χρήσιμο για το Render free tier (keep-alive)
@app.get("/health")
def health():
    return {"status": "alive"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
