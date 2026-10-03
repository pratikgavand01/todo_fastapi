import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from model.sql_model import BASE

load_dotenv()

uri = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER", "postgres"),
    password=os.environ["DB_PASSWORD"],
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME", "to-do-app"),
)

engine = create_engine(uri)
BASE.metadata.create_all(bind=engine)

session = sessionmaker(
    bind=engine,
    autoflush=True,
)

db_session = session()

try:
    connection = engine.connect()
    connection.close()
    print("ping, Connected")
except Exception as e:
    print(f"Error: {str(e)}")