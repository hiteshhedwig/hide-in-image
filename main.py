import numpy as np
import cv2
from hide import HideText, HideInImage, UnHideFromImage


IMAGE_SIZE =  (100, 100, 1)

text = "The rain poured down in torrents, drenching the city streets and turning them into glistening rivers. Umbrellas bobbed up and down like colorful boats amidst the sea of gray, while the rhythmic patter of raindrops on pavement provided a soothing backdrop to the urban symphony. People hurried by, their faces hidden beneath hoods and coats, seeking shelter from the relentless downpour. Yet, amidst the chaos, there was a certain beauty in the way the raindrops danced and shimmered, reflecting the city lights like a mosaic of liquid diamonds."

res = HideText(text)
print(res.get_decoded_text(res.binary))
# print(res.binary)
im = HideInImage(res.binary)
processed =  im.process()
print(processed.shape)

im.save(processed, "coded_img.jpg")


dec = UnHideFromImage(processed)
decoded_str = dec.decode()
# print(decoded_str)
out = res.get_decoded_text(decoded_str)
print(out)