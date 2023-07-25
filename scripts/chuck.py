import requests

# The API endpoint
url = "https://api.chucknorris.io/jokes/random"

try:
    # A GET request to the API
    response = requests.get(url)
except requests.exceptions.HTTPError as error:
    print(error)
    quit()

# find and parse the chuck fact
response_json = response.json()
chuckfact = response_json['value'].replace("Chuck Norris", "\x1b[38;5;39mChuck Norris\x1b[0m") # a little ansi coloring

print(">>> " + chuckfact)
