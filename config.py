from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13600724")) 
API_HASH = getenv("API_HASH", "ee59fd28d0d065c6b7d105082c6a0ba0")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
SUPPORT = getenv("SUPPORT", "https://t.me/AbishnoiMF")
SESSION_NAME = getenv("SESSION_NAME", None)
