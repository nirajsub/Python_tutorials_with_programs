import base64

with open('hydra.png', 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

print(encoded_image)