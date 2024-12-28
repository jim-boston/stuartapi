from typing import Optional, List
from pydantic import BaseModel, Extra
from datetime import datetime


class StudentCore(BaseModel):
	id: str

	class Config:
		from_attributes = True


class StudentShort(StudentCore):
	utln: Optional[str]
	mobile_phone: Optional[str] = None
	email_address: Optional[str] = None
	is_registered: Optional[bool] = None


class StudentWide(StudentShort):
	first_name: Optional[str]
	middle_name: Optional[str] = None
	last_name: Optional[str] = None


class StudentCreate(StudentWide):
	pass


class StudentAll(StudentWide):
	created_date: Optional[datetime]
	created_by: Optional[str]
	modified_date: Optional[datetime]
	modified_by: Optional[str]
