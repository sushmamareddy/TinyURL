import redis 
import os 
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
redis_cient = redis.Redis.from_url(REDIS_URL, decode_responses=True)
