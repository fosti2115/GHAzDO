import requests

# Access Token
access_token = 'EAACEdEose0cBASyyirEPfkeUXkBxou8CE90rCVc2TmtIUaXbsGzmB1kWSiFBYjFXXxah4EDiDfoiwMfFMFDda20ezXElf7QB9McpKyYK8CTXQz8OYpXcjzswhSpfWiMXv9eIdebQqxr9RmqQpRtCCtfpGBnsWnO0M4A5NCbdwHCZD'

# Przykładowe zapytanie do Facebook Graph API
url = 'https://graph.facebook.com/v15.0/me'
params = {
    'access_token': access_token,
    'fields': 'id,name,email'  # Wybór pól do zwrócenia
}
response = requests.get(url, params=params)

if response.status_code == 200:
    print("Dane użytkownika:")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
