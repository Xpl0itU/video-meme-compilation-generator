from dataclasses import dataclass
from dotenv import dotenv_values


@dataclass
class Config:
    reddit_client_id: str
    reddit_client_secret: str

values = dotenv_values(".env")
config = Config(
    values.get("REDDIT_CLIENT_ID"),
    values.get("REDDIT_CLIENT_SECRET"),
)