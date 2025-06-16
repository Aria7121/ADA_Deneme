import os
from sqlalchemy import create_engine, Column, Integer, String, Date, Time, DateTime
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import JSON 
#sql lite (Testing)
from sqlalchemy.sql import func
# API Keys 
from dotenv import load_dotenv
load_dotenv()

# SQLite engine (no username/password or .env needed)
engine = create_engine("sqlite:///local.db", echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ✅ Get environment variables using os.environ.get
#db_user = os.environ.get("DB_USER")
#db_password = os.environ.get("DB_PASSWORD")


# url = URL.create(
#     drivername="postgresql",
#     username=db_user,
#     password=db_password,
#     host="localhost",
#     database="adademo",
#     port=5432
# )

# engine = create_engine(url)
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()

class Conversation(Base):
    __tablename__ = "new_reservations"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    name = Column(String)
    surname = Column(String)
    date = Column(String) #switch to Date
    time = Column(String) # You can later switch to Time
    reservation_type = Column(String)
    party_size = Column(String)
    status = Column(String, default="confirmed")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


Base.metadata.create_all(engine)