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
    display_name = random_critic["display_name"]
    return random_critic, display_name


def critics_reviews(id):
    """
    - get display name
    - concatenate first%20middle%20last
    - append to URL 
    - return reviews
    """
    return get_critics(id=id)