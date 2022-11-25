from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13412363")) 
API_HASH = getenv("API_HASH", "2363839f7780d48f27c9c01bb1a0d01b")
BOT_TOKEN = getenv("BOT_TOKEN", "5385446612:AAHaBL6-WhnUTPmfLKDscwWAgJtSOTnbgIk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5156537452").split()))
SUPPORT = getenv("SUPPORT", "venombot_support")
SESSION_NAME = getenv("SESSION_NAME", "BQApQN9MypJf3wgOT0aUW9X2k1t0V5w4UAMOAoXnbskK6JOyDNwTubSVM4b1sIXMk4z3kzySvCqlWHyVUQIxuUSZ2bN2KKBYu7kzKNrXh0CoqO0lrd0238JvWJWm8IEsuZlqSZyEsDXnNL32z6rMPxSoIclgsZ_VhDhIioAKlYa8uWyxbDuL3SovIki0pnXt2CXDKr_9Dn96D1DM19m6O8ZLunCGhQuzmaIGSMJvrnh8Yz2EotnbKDI64X2wetv7RFRHd-L5e7LdiMQv6NSCk20OQPe2jnTuHPC0ecp1hLaW1-NW1t6VQTnmvXDAKoLYqBV1ydH5KXv3o5FavNKi6xBCAAAAATqo2hEA")
