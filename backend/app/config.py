import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.environ["MONGODB_URL"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
