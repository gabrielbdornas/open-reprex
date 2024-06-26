from requests import post
import os
from dotenv import load_dotenv
import json
load_dotenv()

api_url = "https://sydle-c12404o-treinamento.sydle.one/api/1/crmgabrieldornas/one.sydle_treinamento.sydle.crm/PessoaGabrielDornas/_search/"
your_token = os.getenv("SYDLE-TOKEN")
headers = {
    "Authorization": f"Bearer {your_token}"
}

response = post(
    api_url,
    headers=headers,
)

data_dict = {
  "nome": "Frederico Assis",
  "cPF": "360.365.170-76",
  "sexo": "masculino",
}

# size por padrão é 10

import ipdb;ipdb.set_trace(context=10)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: API call failed with status code {response.status_code}")
    json.loads(response.text)
    error_messages = json.loads(response.text)
    for message in error_messages['generalMessages']:
        print(message['text'])
    for message in error_messages['_messages']:
        print(message['text'])

print(f"Error: API call failed with status code {response.status_code}")
