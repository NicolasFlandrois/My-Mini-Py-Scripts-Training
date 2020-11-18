import json
from urllib.request import urlopen
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Worldwide statistics
url = "https://corona-stats.online?format=json"


with urlopen(url) as f:
    data = f.read()

raw_data = json.loads(data)
# pp.pprint(raw_data)
print("raw_data\t", type(raw_data))
# pp.pprint(raw_data["worldStats"])
print("raw_data['worldStats']\t", type(raw_data["worldStats"]))
# pp.pprint(raw_data["data"][1])  # India exemple
print("raw_data['data']\t", type(raw_data["data"]))
print("raw_data['data'][1]\t", type(raw_data["data"][1]))

# Filter down to 1 Country
# France
# Possible Methode 1
# for i, n in enumerate(raw_data["data"]):
#     if raw_data["data"][i]['country'] == 'France':
#         france = raw_data["data"][i]

# Possible Method 2
for n in raw_data["data"]:
    if n['country'] == 'France':
        france = n

print("France\t", type(france))
print("France :\n")
pp.pprint(france)
print("\n\n")

# China
for n in raw_data["data"]:
    if n['country'] == 'China':
        china = n

print("China\t", type(china))
print("China :\n")
pp.pprint(china)
print("\n\n")

# USA's state by state Case Study

for n in raw_data["data"]:
    if n['country'] == 'USA':
        us_of_a = n

print("us_of_a global stats:\t", type(us_of_a),'\n')
pp.pprint(us_of_a)
print()

url_usa = "https://corona-stats.online/states/us?format=json"


with urlopen(url_usa) as f:
    data = f.read()

us_data = json.loads(data)

print("USA State by State Stats:\n")
pp.pprint(us_data)
print()

def us_of_a_state(state):
    """Printing Covid 19 statistics for a specific State, and returning those
    stats as a dictionary"""
    for n in us_data["data"]:
        if n['state'] == state:
            state_stats = n
    return state_stats

Texas = us_of_a_state("Texas")
print("Covid 19 Stats for US state of:\tTexas")
pp.pprint(Texas)
print()


# Comparing France to USA and US States - Case study
var_Fr = f'{france["deaths"]:,.0f}'.replace(',', ' ')
var_Cn = f'{china["deaths"]:,.0f}'.replace(',', ' ')
var_USA = f'{us_of_a["deaths"]:,.0f}'.replace(',', ' ')
print(f"\nCovid Deaths Counts\nFrance :\t\t{var_Fr}\nChina :\t\t\t{var_Cn}\nUSA :\t\t\t{var_USA}\n===")
# #####
# Auto other countries from List




states = [n['state'] for n in us_data["data"]]

for state in states:
    state_stats = us_of_a_state(state)
    var_usState = f'{state_stats["deaths"]:,.0f}'.replace(',', ' ')
    print(f'State of {state} :\t{var_usState}')
