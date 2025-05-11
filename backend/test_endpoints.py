import requests

#create a command
resp = requests.post(
    "http://localhost:8000/commands",
    json={"id":3, "action":"land", "timestamp":"2025-05-08T12:10:00"}
)

print(resp.status_code, resp.json())

#fetch all commands
resp = requests.get("http://localhost:8000/commands")
print(resp.json())
