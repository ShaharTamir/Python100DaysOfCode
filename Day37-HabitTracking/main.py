from datetime import datetime
import os
import requests

TOKEN = os.environ.get("PIXELA_GRAPH_ONE")
USER_NAME = "shahar"
GRAPH_NAME = "Traiding Graph"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

pixela_sign_up = {
    "token": TOKEN,
    "name": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_sign_up)

user_header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "$",
    "type": "float",
    "color": "shibafu",
}
# response = requests.post(url=pixela_graph_endpoint, headers=user_header, json=graph_config)
date = datetime.today().strftime("%Y%m%d")
graph_post_params = {
    "date": date,
    "quantity": "40"
}

# adding data to the graph
# response = requests.post(url=f"{pixela_graph_endpoint}/{GRAPH_ID}", headers=user_header, json=graph_post_params)
# print(response.text)

updated_data = {
    "quantity": "45"
}

# response = requests.put(url=f"{pixela_graph_endpoint}/{GRAPH_ID}/{date}", headers=user_header, json=updated_data)
# print(response.text)

requests.delete(url=f"{pixela_graph_endpoint}/{GRAPH_ID}/20221115", headers=user_header)
