from pydantic import BaseSettings

from apps.todo.models import Task


class Settings(BaseSettings):
    MONGODB_URL: str
    MONGODB_DATABASE: str

    class Config:
        env_file = ".env"


settings = Settings()

models = [
    Task
]
