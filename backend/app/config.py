from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Shop | Items"
    debug: bool = False
    database_url: str = "sqlite:///./shop.db"

    cors_origin: list = ["*"]

    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file = ".env"


settings = Settings()
