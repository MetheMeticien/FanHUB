from datetime import datetime, timedelta, timezone
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')



def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()

    # Convert expiration time into a timestamp (in seconds)
    expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})

    # Convert to a UNIX timestamp (seconds since epoch) for serializing
    to_encode["exp"] = expire.timestamp()

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
