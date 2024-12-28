import uvicorn
from fastapi import FastAPI

# StuartAPI classes
from common.settings import Settings
from routers.country import router as country_router
from routers.student import router as student_router


settings = Settings()

# notes
# - only a POC with get all and get record
# - No response schemas because I want to have a custom response based on fields passed (didn't know how to make a dynamic response schema)
# - no security
# - SQL Server DB with views for each Model.  I don't perform JOINs in the ORM, I put them in the SQL views
# - I explored creating runtime models and schemas, but stopped because it seemd to much work.  So I have an external generator of Model object classes.

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
