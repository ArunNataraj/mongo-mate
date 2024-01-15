"""Config File"""
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

MONGO_CLIENT_URI = os.getenv("MONGO_CLIENT_URI")
ALGORITHM = os.getenv("ALGORITHM")
TOKEN_SECRET_KEY = os.getenv("TOKEN_SECRET_KEY")
