import requests

url = "http://127.0.0.1:5050/api/bookings/recurring"

data = {
    "room_id": 1,
    "user_id": 1,
    "title": "Cykliczne spotkanie zespołu",
    "description": "Spotkanie co tydzień",
    "start_time": "2026-06-25T10:00:00",
    "end_time": "2026-06-25T11:00:00",
    "recurrence_rule": "WEEKLY",
    "count": 5,
    "attendees_count": 5
}

try:
    response = requests.post(url, json=data)

    print("Status:", response.status_code)
    print("\nTreść odpowiedzi:")
    print(response.text)

except Exception as e:
    print("Błąd podczas wysyłania żądania:")
    print(e)