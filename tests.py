import requests
import json

# Get all Persons

def get_all_persons():
    resposnse= requests.get("https://hngtask2-production.up.railway.app/api").json()
    return resposnse

# Create Person

def create_person(name):
    payload=json.dumps({"name":name})
    created_person=requests.post("https://hngtask2-production.up.railway.app/api",data=payload)
    return created_person.json()


# get single person

def get_person(pk):
    gotten_person=requests.get(f"https://hngtask2-production.up.railway.app/api/{pk}")
    return gotten_person.json()
# delete Person

def delete_person(pk):
    response=requests.delete(f"https://hngtask2-production.up.railway.app/api/{pk}")
    return response.json()

def update_person(pk,name):
    payload=json.dumps({"name":name})
    response=requests.put(f"https://hngtask2-production.up.railway.app/api/{pk}",data=payload)
    return response.json()


# These are some functions calls to test, please dont call them at once ejoor!!!

# create_person("Samson")
# print(delete_person(5))
# print(create_person("JovialCore"))
# print(get_person(5))
# print(get_all_persons())
# print(update_person(4,"Bimbo"))

