import os

from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    mysql_server_name : str = os.environ.get('MYSQL_SERVER_NAME')
    mysql_username    : str = os.environ.get('MYSQL_USERNAME')
    mysql_password    : str = os.environ.get('MYSQL_PASSWORD')
    mysql_database    : str = os.environ.get('MYSQL_DATABASE')
    mysql_port        : int = os.environ.get('MYSQL_PORT')


settings = Settings()
