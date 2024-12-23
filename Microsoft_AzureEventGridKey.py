import requests

event_grid_endpoint = "https://your-event-grid-endpoint.westus2-1.eventgrid.azure.net/api/events"
event_grid_key = "ROiJE97+lzhZr+POeyVsjWXHdZAUrAK54+AEhEQj6ig="

headers = {
    "Content-Type": "application/json",
    "aeg-sas-key": event_grid_key,
}

# Wysłanie przykładowego zdarzenia
event = [
    {
        "id": "1",
        "eventType": "My.Custom.Event",
        "subject": "/example/subject",
        "eventTime": "2023-01-01T00:00:00Z",
        "data": {"key": "value"},
        "dataVersion": "1.0",
    }
]

response = requests.post(event_grid_endpoint, json=event, headers=headers)
print(response.status_code)
