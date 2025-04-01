import requests
from pyzbar import pyzbar
from PIL import Image
import io

url = (
    "https://hackattic.com/challenges/reading_qr/problem?access_token=8c740559b44f2213"
)

response = requests.get(url)
data = response.json()
image_url = data["image_url"]

image_response = requests.get(image_url)
image_data = image_response.content

image = Image.open(io.BytesIO(image_data))
decode_objects = pyzbar.decode(image)
print(decode_objects)
for obj in decode_objects:
    qr_code = obj.data.decode("utf-8")
    print(qr_code)

    submit_url = "https://hackattic.com/challenges/reading_qr/solve?access_token=8c740559b44f2213"
    solution = {"code": qr_code}
    submit_reponse = requests.post(submit_url, json=solution)
    print(submit_reponse.text)
