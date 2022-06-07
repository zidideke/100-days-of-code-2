import requests
import datetime as dt
#This project keep track of your daily habit(e.g studying, workout/exercise etc) using pixels

USERNAME = "chidinma"
TOKEN = "hhsjdhf888sjjeuhh"   #self generated and kept safe
GRAPH_ID = "Graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#Create a user account
## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today=dt.datetime.now()


pixel_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kn did you run today?: ")

}
#POST - /v1/users/<username>/graphs/<graphID>

pixel_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/graph1"


response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

#https://pixe.la/v1/users/chidinma/graphs/graph1.html    #shows the pixel when put on the browser

#response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
#print(response.text)
#today=dt.datetime(year=2022, month=5, day=29)
# date ="today.strftime('%Y%m%d')"
#
# #to update a pixel
# pixel_update_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220529"
#
# new_pixel_data= {
#     "quantity": "10.2"
# }
#
# #response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# #print(response.text)
#
# #Delete a pixel
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220601"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)