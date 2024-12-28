from typing import Optional, List
from pydantic import BaseModel, Extra
from datetime import datetime


class CountryCore(BaseModel):
	id: str

	class Config:
		from_attributes = True


class CountryShort(CountryCore):
	name: Optional[str]


class CountryWide(CountryShort):
	status: Optional[str]
	order: Optional[int]


class CountryCreate(CountryWide):
	pass


class CountryAll(CountryWide):
	created_date: Optional[datetime]
	created_by: Optional[str]
	modified_date: Optional[datetime]
	modified_by: Optional[str]
