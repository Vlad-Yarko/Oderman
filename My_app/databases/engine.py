from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

engine = create_async_engine(url=os.getenv('DB'), echo=True)
main_session = async_sessionmaker(bind=engine)
