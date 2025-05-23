from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRET_KEY: str
    HASH: str

    class Config:
        env_file = '.env'

setting = Settings()

DATABASE_URL = f"postgresql+asyncpg://{setting.DB_USER}:{setting.DB_PASS}@{setting.DB_HOST}:{setting.DB_PORT}/{setting.DB_NAME}"
SECRET=setting.SECRET_KEY
HASH=setting.HASH