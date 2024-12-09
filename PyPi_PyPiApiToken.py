import requests

api_token = "pypi-AgEIcHlwaS5vcmcCJDdiODk1ZGQ5LWNkYzQtNGE4Yi04OWJkLWE2N2NlODMwZWI4NgACKlszLCJmZmY3ZDViOS00MGE1LTQ0YmEtYTM0My0yMzRiNzZmNjM4MWMiXQAABiD95sTmlEcEW94Ek1wPrzwpmCivReKx-R0IcJiILuIYaQ"
package_name = "example-package"

headers = {
    "Authorization": f"token {api_token}",
    "Accept": "application/json",
}

# Pobranie informacji o pakiecie z PyPi
response = requests.get(f"https://pypi.org/pypi/{package_name}/json", headers=headers)
print(response.json())
