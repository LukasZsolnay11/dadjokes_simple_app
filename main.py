import requests
from random import choice
import pyfiglet
from termcolor import colored


header = pyfiglet.figlet_format("DAD JOKES")
header = colored(header, color="magenta")
print(header)

user_input = input("What kind of jokes you search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(url, headers={"Accept": "application/json"},
                   params={"term":user_input}).json()

num_jokes = len(res["results"])
num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here is one: ")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke about {user_input}. Here is: ")
    print(res(results[0]["joke"]))
else:
    print(f"Sorry, couldnt find a joke with your term: {user_input}")