from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import text
import time
import os
from common.settings import Settings


settings = Settings()

print("username", settings.username)
print("password", settings.password)
print("host", settings.host)
print("database", settings.database)


connection_url = URL.create(
    "mssql+pyodbc",
    username=settings.username,
    password=settings.password,
    host=settings.host,
    database=settings.database,
    query={"driver": "ODBC Driver 17 for SQL Server"},
)
print(connection_url)

engine = create_engine(
    connection_url,
    implicit_returning=False,
    echo=True
)

conn = engine.connect()

result = conn.execute(text("select * from ExtendedField WHERE FieldName LIKE 'ca%' ORDER BY TableName, FieldName"))
for row in result:
    print("FieldName:", row.TableName + "." + row.FieldName)

result.close()

conn.close()

while True:
    print(".", end='')
    time.sleep(1)
