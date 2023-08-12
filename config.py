from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13412363")) 
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "520")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150000"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5156537452").split()))
SUPPORT = getenv("SUPPORT", "venombot_support")
SESSION_NAME = getenv("SESSION_NAME", "")
