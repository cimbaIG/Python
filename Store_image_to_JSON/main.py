import json
import base64

# Store image to JSON object
data = {}
with open('./Test_figures/zadatak_1.pdf', mode='rb') as file:
    img = file.read()
data['img'] = base64.encodebytes(img).decode('utf-8')

print(json.dumps(data))

# Get image back from JSON and store it to some image file type
with open("./Decoded_figures/decoded_zadatak_1.pdf", "wb") as fh:
    fh.write(base64.b64decode(data['img']))