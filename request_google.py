import requests
response = requests.get("https://google.com")
print(f"Response is: {response}")
x = len(response.text)
print(f"Length of response is: {x}")
