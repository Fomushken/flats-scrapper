from dataclasses import dataclass
from environs import Env

@dataclass
class DBConfig:
    databate: str
    db_host: str
    db_user: str
    db_password: str

@dataclass
class TgBot:
    token: str
    admin_ids: str

@dataclass
class RedisConfig:
    url: str

@dataclass
class Config:
    tg_bot: TgBot
    db: DBConfig
    redis: RedisConfig



def load_config(path: str | None = None) -> Config:
    
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db=DBConfig(
            databate=env("DATABASE"),
            db_host=env("DB_HOST"),
            db_user=env("DB_USER"),
            db_password=env("DB_PASSWORD")
        ),
        redis=RedisConfig(
            url=env("REDIS_URL")
        )
    )
