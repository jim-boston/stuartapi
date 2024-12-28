from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

# StuartAPI classes
from common.settings import Settings


settings = Settings()

print("username", settings.username)
print("password", settings.password)
print("host", settings.host)
print("database", settings.database)

connection_url = URL.create(
    "mssql+pyodbc",
    #    username="admin",
    #    password="tpifDOG!",
    #    host="mc-consmgr.cvpf5emrbdmm.us-east-1.rds.amazonaws.com",
    #    database="mc-consmgr",
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

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = SessionLocal()
    yield session


Base = declarative_base()
