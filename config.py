from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13412363")) 
API_HASH = getenv("API_HASH", "2363839f7780d48f27c9c01bb1a0d01b")
BOT_TOKEN = getenv("BOT_TOKEN", "5206815916:AAEmQbjkVBSVl71mr4aLxvTgoF_nZ3BrDfo")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150000"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5156537452").split()))
SUPPORT = getenv("SUPPORT", "venombot_support")
SESSION_NAME = getenv("SESSION_NAME", "BQBySTGEarwb1NDQKcSuxwxEYJoVHqEtuZkac6TyqFmkrrOtLP5HwUqAn3ByiRpUcL5MpYVP45gBmEERENtWujhUCa7haHq9LB8yp0uL_sUNHMVtC3fpKi7pXiPTs2CT8iWyb2d8cWnQ5gPS6B7cEzLZun1ZVPsRknNBesaJT72Glt8EItrF4pojOgWvG7OWZiGFIL0IFgRZl8qDXOuxmWhYNvu7jRuLf7uUiQDSELH9WiRoibuzHVbvq0kH8DD3M9TegmX9gxPI6QgMrxwfuQKQb73BzGHh8LGZoliYg7er4y9--JK2FIvOqp3NHIf8EOmEpzi-Fr4g9R1XZVIhBBc1AAAAATqo2hEA")
