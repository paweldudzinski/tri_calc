from stravalib import Client
from .lib.strava_auth import StravaAuth
from .lib.strava_api import StravaAPI
from .lib.dtos import StravaClientData


client = Client()
strava_client_data = StravaClientData(
    11915,
    'f4c60c08627b7475b805672d4dc8491f47230240')
strava_auth = StravaAuth(
    client,
    strava_client_data,
    'http://127.0.0.1:6543/authorize')
strava_api = StravaAPI(client)
