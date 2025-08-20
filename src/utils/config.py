from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    GIE_API_KEY: str
    DATA_DIR: Path = Path("data")
    RAW_DIR: Path = Path("data/raw")
    CURATED_DIR: Path = Path("data/curated")
    HDD_CITIES: str | None = None  # "City:lat,lon,alt;City2:lat,lon,alt"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
settings.RAW_DIR.mkdir(parents=True, exist_ok=True)
settings.CURATED_DIR.mkdir(parents=True, exist_ok=True)
