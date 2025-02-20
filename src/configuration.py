from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    database_url: str
    postgres_user: str
    postgres_password: str
    postgres_db: str

    class Config:
        env_file = "../.env_example"
        env_file_encoding = "utf-8"


appsettings = AppSettings()
