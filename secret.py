import os

class Secret:
    # email = "gcarricaballero3@hotmail.com"
    # password = "Jacob2016@"
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")