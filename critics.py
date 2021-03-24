import requests
from requests.auth import HTTPBasicAuth
import random

id = ""
url = f"https://api.nytimes.com/svc/movies/v2/critics/{id}.json"
params = {'api-key':'9eU3GwocQRJ3rOcFjBMAYh5MRUAh5WbG'}


def get_critics(id="all"):
    response = requests.get(url, params=params)
    return response.json(), response.json()["num_results"]


def pick_random_critic(id):
    all, number_of_all = get_critics(id)
    pick_one = random.randint(0, number_of_all)
    random_critic = all["results"][pick_one]
    return random_critic