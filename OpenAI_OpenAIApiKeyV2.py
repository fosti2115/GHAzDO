import openai

api_key = "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"

# Ustawienie klucza API
openai.api_key = api_key

# Zapytanie o dostępne modele
models = openai.models.list()

# # Wyświetlenie dostępnych modeli
for model in models.data:
     print(model.id)

# Zapytanie do modelu (używamy `completions.create` zamiast `ChatCompletion`)
response = openai.completions.create(
    model="gpt-3.5-turbo",  # Lub gpt-3.5-turbo
    prompt="Wytłumacz działanie klucza API w Pythonie.",
    max_tokens=100
)

# Wyświetlenie odpowiedzi
print(response['choices'][0]['text'].strip())
