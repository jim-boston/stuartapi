from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
import json

# StuartAPI classes
from common.db import get_session
from schemas.country import *
from schemas.options import CountryOptions
from services import country as country_services


router = APIRouter()

@router.get("/countries/")
def get_countries(
        skip: int = 0,
        limit: int = 100,
        fields: str = None,
        session: Session = Depends(get_session)):

    options = CountryOptions()
    options.skip = skip
    options.limit = limit
    options.fields = fields

    country_data = country_services.read_all(session, options=options)

    if country_data is None:
        raise HTTPException(status_code=404, detail="Countries not found")

    # stream the data
    for row in country_data:
        yield row._asdict()

@router.get("/countries/{id}")
def get_country(
        id: str,
        fields: str = None,
        session: Session = Depends(get_session)):

    options = CountryOptions()
    options.fields = fields

    country_data = country_services.read(session, id=id, options=options)
    
    if country_data is None:
        raise HTTPException(status_code=404, detail="Country not found")

    # stream the data
    return country_data._asdict()
