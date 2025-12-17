import json
import urllib.request
import random
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Get all Pokémon
url = "https://pokeapi.co/api/v2/pokemon?limit=2000"
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

pokemon = [p["name"] for p in data["results"]]

# Choose ONCE
pokemonName = random.choice(pokemon)
print("name:", pokemonName)

# Use the SAME name
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemonName}"
with urllib.request.urlopen(pokemon_url) as response:
    data = json.loads(response.read().decode())

abilities = [a["ability"]["name"] for a in data["abilities"]]
print("abilities:", abilities)
