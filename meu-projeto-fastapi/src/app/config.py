from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Minha API FastAPI"
    admin_email: str = "admin@example.com"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()