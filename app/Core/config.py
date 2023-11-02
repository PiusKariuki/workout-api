import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = 'WORKOUT API'
    PROJECT_VERSION: str = '1.0.0'

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    SALT: str = os.getenv("SALT")

    DEMO_EMAIL:str = os.getenv("DEMO_EMAIL")

    API_NINJAS_KEY: str = os.getenv("API_NINJAS_KEY")


settings = Settings
