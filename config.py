import os 
from dotenv import load_dotenv

load_dotenv()

GOOGLE_CLIENT_ID = os.environ.get('client_id', None)
GOOGLE_CLIENT_SECRET = os.environ.get('client_secret', None)