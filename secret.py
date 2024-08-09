import os

class Secret:
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")