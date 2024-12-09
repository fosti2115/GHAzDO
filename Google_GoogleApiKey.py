import openai
import requests

# Ustawienie poświadczeń
google_api_key = 'XXX'

# Przykładowe zapytanie do Google API (np. Google Search API)
url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q': 'OpenAI',
    'key': google_api_key,
    'cx': 'your_custom_search_engine_id',
}
response = requests.get(url, params=params)
print(response.json())
