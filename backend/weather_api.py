from fastapi import FastAPI
from data_manager import get_weather_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with a specific domain for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "weather root"}

@app.get("/weather_data")
async def weather_data():
    weather_data = get_weather_data()
    return weather_data