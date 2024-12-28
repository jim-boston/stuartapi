import uvicorn
from fastapi import FastAPI

# custom modules
from routers import country


app = FastAPI()
app.include_router(country.router)

@app.get("/")
async def root():
    return {"message": "StuartAPI v.01"}

@app.get("/health")
async def health():
    return {"message": "Healthy"}

# run hosting
uvicorn.run(app, host="0.0.0.0", port=8000)