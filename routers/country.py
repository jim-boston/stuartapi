from fastapi import Depends, APIRouter, HTTPException

router = APIRouter()

@router.get("/countries/{country_code}")
def get_country(
        country_code: str,
        fields: str = None):

    if country_code == "US":
        return {"country": "US", "Name": "United States of America"}
    else:
        return {"error": "Unknown country"}
