import numpy as np 
import cv2

def hide_message(image, message):
    image_array = np.array(image)
    message_binary = message.encode('utf-8').hex()
    message_binary = message_binary.ljust(len(image_array) * 8, '0')
    
    for i in range(len(image_array)):
        pixel_lsb = image_array[i] & 1
        image_array[i] = image_array[i] >> 1 | message_binary[i // 8]
    return image_array
def reveal_message(image):
    image_array = np.array(image)
    message = ''
    for i in range(len(image_array)):
        pixel_lsb = image_array[i] & 1
        message += str(pixel_lsb)
    return message.decode('utf-8')
image = cv2.imread('logo.jpeg')
image_array = np.array(image)
image_array = hide_message(image_array, 'no module found')
cv2.imwrite('logo.jpeg', image_array)
message = reveal_message(image)
print(message)