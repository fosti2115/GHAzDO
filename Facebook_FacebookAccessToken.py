import requests

# Access Token
access_token = '1629363414282776kxhTy3rKUAfMubhpvtgHn6aj1_Ro'

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
