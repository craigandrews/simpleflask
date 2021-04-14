import requests
from requests.auth import HTTPBasicAuth
import random

id = ""
URL = f"https://api.nytimes.com/svc/movies/v2/critics/{id}.json"
params = {'api-key':'9eU3GwocQRJ3rOcFjBMAYh5MRUAh5WbG'}


def get_critics(id="all"):
    response = requests.get(URL, params=params)
    return response.json(), response.json()["num_results"]


def pick_random_critic(id):
    all, number_of_all = get_critics(id)
    pick_one = random.randint(0, number_of_all-1)
    random_critic = all["results"][pick_one]
    display_name = list(random_critic["display_name"])
    return random_critic, display_name


def name_to_url():
    display_name = pick_random_critic(id)[1]
    names = []
    for n in display_name:
        if n != ' ':
            names.append(n)
        elif n == ' ':
            names.append("%20")
    url_suffix = ''.join(names)
    return url_suffix

def individual_critic(id):
    critic_name = name_to_url()
    URL = f"https://api.nytimes.com/svc/movies/v2/critics/{critic_name}.json"
    response = requests.get(URL, params=params)
    print(URL)
    return response.json()