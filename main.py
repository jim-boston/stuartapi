import uvicorn
from fastapi import FastAPI

# custom modules
from routers import country


app = FastAPI()
app.include_router(country.router)

@app.get("/")
async def root():
    return {"message": "StuartAPI v.1"}

@app.get("/health")
async def health():
    print('health endpoint')

# run hosting
uvicorn.run(app, host="0.0.0.0", port=8000)