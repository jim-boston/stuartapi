from sqlalchemy import Column, Integer, String, Boolean, DateTime

# StuartAPI classes
from common.db import Base


class CountryModel(Base):
	__tablename__ = 'api__country'
	id = Column(String[2],  nullable=False, primary_key=True, name='Country')
	name = Column(String[50],  nullable=True, primary_key=False, name='CountryName')
	status = Column(String[15],  nullable=True, primary_key=False, name='Status')
	order = Column(Integer,  nullable=True, primary_key=False, name='DisplayOrder')
	created_date = Column(DateTime,  nullable=True, primary_key=False, name='CreatedDate')
	created_by = Column(String[32],  nullable=True, primary_key=False, name='CreatedBy')
	modified_date = Column(DateTime,  nullable=True, primary_key=False, name='ModifiedDate')
	modified_by = Column(String[32],  nullable=True, primary_key=False, name='ModifiedBy')

	def resolve_fields(fields: str):

		# get columns form field list using the required and defaults
		fields = ["id", "name"] if fields is None else fields.split(",")
		return [getattr(CountryModel, field) for field in fields]
