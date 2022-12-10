from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13412363")) 
API_HASH = getenv("API_HASH", "2363839f7780d48f27c9c01bb1a0d01b")
BOT_TOKEN = getenv("BOT_TOKEN", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5156537452").split()))
SUPPORT = getenv("SUPPORT", "venombot_support")
SESSION_NAME = getenv("SESSION_NAME", ")
