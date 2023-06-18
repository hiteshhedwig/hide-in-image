import numpy as np
import cv2
from hide import HideText, HideInImage, UnHideFromImage


IMAGE_SIZE =  (100, 100, 1)

text = "This was an introductory lesson to building android apps in python. We learned what is Kivy, why, and how to use environments, built a basic app in Kivy, compared Kivy and Kivymd with an example of a button code. In the next article, we will continue our journey and explore various other key elements in Kivymd. If you liked this article, follow me on medium so you receive notifications about upcoming parts. With that said sayonara!"

res = HideText(text)
print(res.get_decoded_text(res.binary))
print(res.binary)
im = HideInImage(res.binary)
processed =  im.process()
print(processed.shape)

im.save(processed, "coded_img.jpg")


dec = UnHideFromImage(processed)
decoded_str = dec.decode()
print(decoded_str)
out = res.get_decoded_text(decoded_str)
print(out)