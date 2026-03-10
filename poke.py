import requests
import json

proxy = {
    "https": "http://proxy.spo.ifsp.edu.br:3128",
    "http": "http://proxy.spo.ifsp.edu.br:3128"
}

limit = input("Limit pokemons: ")

params = {"limit": limit}

try:
    r = requests.get("https://pokeapi.co/api/v2/pokemon",params=params ,proxies=proxy)
    print(r.status_code)
except requests.exceptions.ProxyError as e:
    print(f"Proxy error {e}")
    exit()

data = r.json()
print(data.keys())
pokemons = data["results"]

# Name from first 50 pokemons
for i in range(len(pokemons)):
    print(pokemons[i]["name"])


pokemon = input("Digit the pokemon you want to search for: ").strip()

try:
    # Passing path parameters
    p = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}", proxies=proxy)
    print(p.status_code)
except requests.exceptions.ProxyError as e:
    print(f"Proxy error: {e}")
    exit()

try:
    pokemon_data = p.json()
except json.decoder.JSONDecodeError:
    print(f"Not Found")
    exit()
print(pokemon_data["stats"])
