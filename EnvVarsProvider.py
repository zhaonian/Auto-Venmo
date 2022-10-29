from asyncio import constants
from typing import List
from Constants import *
from dotenv import load_dotenv
from os import environ

# Provides the varaible data from .env
class EnvVarsProvider:

    def __init__(self):
        load_dotenv()
    
    def get_venmo_acess_token(self):
        return environ[VENMO_ACCESS_TOKEN]

    def get_cricket_friends_usernames(self) -> List:
        return [environ[DAVIS], environ[DAVIS]]
