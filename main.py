#  A custom website using API
# just for fanatics

import requests
import os
from dotenv import load_dotenv
import pandas as pd


URL = 'https://the-one-api.dev/v2/character/'

# Environment variables
load_dotenv('.env')
API_KEY = os.getenv('OWM_API_KEY')

parameters = {
    'Authorization': f'Bearer {API_KEY}',
}

requests_data = requests.get(URL, headers=parameters)

data_json = requests_data.json()
data = data_json['docs'][:]

df = pd.DataFrame(data)

# noinspection PyTypeChecker
df.to_csv('lord_of_the_rings.csv', encoding="utf-8-sig")
