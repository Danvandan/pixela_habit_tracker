import requests
from datetime import datetime
USERNAME = "danvandan890"
TOKEN = "dan1the2man3likes4cold5ham6"
GRAPH1 = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"


}

#response=requests.post(url=pixela_endpoint, json=user_params)
#print(response.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH1,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers =  {
    "X-USER-TOKEN": TOKEN

}

#response = requests.post(url=graph_endpoint, json=graph_config,headers=headers)
#print(response.json())

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1}"

today = datetime.now()
print(today.strftime("%Y%m%d"))


pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

#response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
#print(response.json())

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1}/{today.strftime('%Y%m%d')}"

update_pix_config = {
    "quantity": "66.6"
}

response = requests.put(url=update_pixel_endpoint, json=update_pix_config, headers=headers)
print(response.json())