import numpy as np
import cv2
import tqdm
import math

class HideText(object):
    def __init__(self, text):
        self.binary = self.str_to_binary(text)

    @staticmethod
    def str_to_binary(string):
        binary_paragraph = ''.join(format(ord(char), '08b') for char in string)
        return binary_paragraph
    
    @staticmethod
    def get_decoded_text(binary):
        decoded_string = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
        return decoded_string
    
    def __repr__(self) -> str:
        return self.binary

    def __len__(self):
        return len(self.binary)
    
class HideInImage(object):
    def __init__(self, binary_eqv):
        IMAGE_SIZE =  self.get_image_size(binary_eqv)
        self.binary_eqv = binary_eqv
        self.image = np.zeros(IMAGE_SIZE, dtype=np.float32) + [0]#*255
        
    def get_image_size(self, binary_size):
        size = binary_size
        a = len(str(size))*2
        closest = math.ceil(math.sqrt(a))
        return (closest,closest)


    def process(self):
        print("Processing ")
        shape = self.image.shape

        count = 0
        total_binary_bytes = len(self.binary_eqv)
        print(total_binary_bytes)
        for row in tqdm.tqdm(range(0, shape[0])):
            for col in range(0, shape[1]):
                if (row%2) == 0:
                    if count < total_binary_bytes:
                        self.image[row][col] = int(self.binary_eqv[count])
                        count += 1

        self.image = self.image*255
        img_merged = cv2.merge((self.image,self.image,self.image))
        return img_merged

    def save(self, image, filename):
        cv2.imwrite(filename, image)


class UnHideFromImage(object):
    def __init__(self, image):
        self.image = image
        
    def decode(self):
        print("Processing ...")
        image = self.image[:,:,0]
        shape = image.shape

        binary_str = ""
        last_one_idx = None
        for row in tqdm.tqdm(range(0, shape[0])):
            for col in range(0, shape[1]):
                if (row%2) == 0:
                    val = int(image[row][col]/255)
                    binary_str = binary_str+str(val)
                    if val == 1 :
                        last_one_idx = val


        # print(binary_str)

        return binary_str[:]
