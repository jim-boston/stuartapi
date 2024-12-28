from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, DataError

# StuartAPI classes
from common.db import Base
from models.country import CountryModel
from schemas.country import *
from schemas.options import CountryOptions


def read_all(session: Session,
    options: CountryOptions = CountryOptions()):

    columns = CountryModel.resolve_fields(options.fields)

    sql = (select(*columns)
        .order_by(CountryModel.id)
        .offset(options.skip)
        .limit(options.limit))

    country_data = session.execute(sql)

    return country_data

def read(session: Session,
    id: str,
    options: CountryOptions = CountryOptions()):

    columns = CountryModel.resolve_fields(options.fields)

    sql = (select(*columns)
        .filter(CountryModel.id == id)
        .limit(1))

    country_data = session.execute(sql).fetchone()

    return country_data

