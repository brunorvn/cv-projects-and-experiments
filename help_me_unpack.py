import requests
import struct

url = "https://hackattic.com/challenges/help_me_unpack/problem?access_token=8c740559b44f2213"

response = requests.get(url)
data = response.json()
print(data)


