from fastapi import FastAPI

from config.database import init_db

from apps.todo.routes import router as todo_router

app = FastAPI()


@app.on_event("startup")
async def connect():
    await init_db()
    print("Database initialized.")


app.include_router(todo_router)
