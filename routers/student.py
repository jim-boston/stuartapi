from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session

# StuartAPI classes
from common.db import get_session
from schemas.student import *
from schemas.options import StudentOptions
from services import student as student_services


router = APIRouter()

@router.get("/students/")
def get_students(
        skip: int = 0,
        limit: int = 100,
        fields: str = None,
        is_registered: bool = None,
        grad_year: str = None,
        session: Session = Depends(get_session)):

    options = StudentOptions()
    options.skip = skip
    options.limit = limit
    options.fields = fields
    options.is_registered = is_registered
    options.grad_year = grad_year

    student_data = student_services.read_all(session, options=options)

    if student_data is None:
        raise HTTPException(status_code=404, detail="Students not found")

    # return the data
    for row in student_data:
        yield row._asdict()

@router.get("/students/{id}")
def get_student(
        id: str,
        fields: str = None,
        session: Session = Depends(get_session)):

    options = StudentOptions()
    options.fields = fields

    student_data = student_services.read(session, id=id, options=options)

    if student_data is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student_data._asdict()

