import uvicorn
from fastapi import FastAPI

# StuartAPI classes
from common.settings import Settings
from routers.country import router as country_router
from routers.student import router as student_router


settings = Settings()

app = FastAPI()
app.include_router(country_router)
app.include_router(student_router)

@app.get("/")
async def root():
    return {"message": "StuartAPI v0.02"}

@app.get("/health")
async def health():
    return {"message": "Healthy"}

# run hosting
uvicorn.run(app, host="0.0.0.0", port=8000)
