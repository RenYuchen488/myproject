import requests

print("Hello, VS Code!")
response = requests.get("https://api.github.com")
print(f"Status code: {response.status_code}")