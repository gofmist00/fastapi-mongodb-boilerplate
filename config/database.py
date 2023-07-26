import certifi
from beanie import init_beanie
import motor.motor_asyncio

from config.settings import settings, models

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGODB_URL, uuidRepresentation="standard", tlsCAFile=certifi.where()
)
db = client[settings.MONGODB_DATABASE]


async def init_db():
    await init_beanie(
        database=db,
        document_models=models,
    )

    print("Database Initialize")
