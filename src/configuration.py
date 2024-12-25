from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env_example"
        env_file_encoding = "utf-8"


appsettings = AppSettings()
