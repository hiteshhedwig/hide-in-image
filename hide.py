import numpy as np
import cv2
import tqdm

class HideText(object):
    def __init__(self, text):
        self.binary = self.str_to_binary(text)

    @staticmethod
    def str_to_binary(string):
        # Initialize empty list to store binary values
        binary_list = []
        # Iterate through each character in the string
        for char in string:
            # Convert character to binary, pad with leading zeroes and append to list
            binary_list.append(bin(ord(char))[2:].zfill(8))         
        # Join the binary values in the list and return as a single string
        return ''.join(binary_list)
    
    @staticmethod
    def get_decoded_text(binary):
        input_string=int(binary, 2);
        total_bytes= (input_string.bit_length() +7) // 8
        input_array = input_string.to_bytes(total_bytes, "big")
        return input_array.decode()
    
    def __repr__(self) -> str:
        return self.binary

    def __len__(self):
        return len(self.binary)
    
class HideInImage(object):
    def __init__(self, binary_eqv):
        IMAGE_SIZE =  (100, 100)
        self.image = np.zeros(IMAGE_SIZE, dtype=np.float32) + [0]#*255
        self.binary_eqv = binary_eqv
        
    def process(self):
        print("Processing ")
        shape = self.image.shape

        count = 0
        total_binary_bytes = len(self.binary_eqv)

        for row in tqdm.tqdm(range(0, shape[0])):
            for col in range(0, shape[1]):
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
        last_one_index = None
        for row in tqdm.tqdm(range(0, shape[0])):
            for col in range(0, shape[1]):
                if int(image[row][col]) == 119:
                    break
                val = int(image[row][col]/255)
                binary_str = binary_str+str(val)
                print(val)

        return binary_str
