import numpy as np
import cv2

def hide_message(img, message):
    image_array = np.array(img)
    message_binary = message.encode('utf-8')
    message_binary = message_binary.ljust(len(image_array))
    
    for i in range(len(image_array)):
        pixel_lsb = image_array[i] & 1
        image_array[i] = image_array[i] >> 1 | message_binary[i]

    return image_array, message_binary

def reveral_message(img, message_binary):
    image_array = np.array(img)
    message = ''
    for i in range(len(image_array)):
        pixel_lsb = image_array[i] & 1
        message += str(pixel_lsb)
    return message_binary.decode('utf-8'), message.encode('utf-8')


if __name__ == '__main__':
    pesan = input('Masukan Pesan Untuk Disembunyikan Ke gambar:')
    image = cv2.imread('logo.jpeg')
    image_hide, message_hide = hide_message(image,pesan)
    cv2.imwrite('logo.jpeg', image_hide)

    # menampilkan pesan nya
    message_hide, message = reveral_message(image, message_hide)
    print(message_hide)