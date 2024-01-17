import requests
import json
import pprint 

url =
show = input("please input a show name.>")
params = {"q":"Girls"}

if response.status_code == 200:
    data = json.loads(respsone.text)
    #pprint.pprint(data)

    name = data['name']
    premiered = data['premiered']
    summary = data['summary']

    print(f"{name} premiered on {premiered}.")
    print(f"{name}" ending: {summary:}")


else:
    print(f"Error: {response.status_code}")

