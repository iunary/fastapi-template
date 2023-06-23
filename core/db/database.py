from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from core.settings import settings

engine = create_engine(settings.BATABASE_URL)
session: Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
