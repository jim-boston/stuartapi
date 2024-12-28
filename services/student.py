from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, DataError

# StuartAPI classes
from common.db import Base
from models.student import StudentModel
from schemas.student import *
from schemas.options import StudentOptions


def read_all(session: Session,
    options: StudentOptions = StudentOptions()):

    columns = StudentModel.resolve_fields(options.fields)

    sql = select(*columns)

    # filter by registration
    if options.is_registered is not None:
        sql = sql.filter(StudentModel.is_registered == options.is_registered)

    # filter by graad year
    if options.grad_year is not None:
        sql = sql.filter(StudentModel.grad_year == options.grad_year)

    # finish query
    sql = (sql
        .order_by(StudentModel.id)
        .offset(options.skip)
        .limit(options.limit))

    student_data = session.execute(sql)

    return student_data

def read(session: Session,
    id: str,
    options: StudentOptions = StudentOptions()):

    columns = StudentModel.resolve_fields(options.fields)

    sql = (select(*columns)
        .filter(StudentModel.id == id)
        .limit(1))

    student_data = session.execute(sql).fetchone()

    return student_data
