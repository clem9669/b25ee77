

from PIL import Image, ImageFont, ImageDraw

from bitstring import BitStream

def decode_image(file_location="lsb_RGB.png"):
    """Decodes the hidden message in an image

    file_location: the location of the image file to decode. By default is the provided encoded image in the images folder
    """
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]
    green_channel = encoded_image.split()[1]
    blue_channel = encoded_image.split()[2]

    b = BitStream()

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if red_channel.getpixel((i, j)) & 1 == 1:
                b.append('0b1')
            else:
                b.append('0b0')
            if green_channel.getpixel((i, j)) & 1 == 1:
                b.append('0b1')
            else:
                b.append('0b0')
            if blue_channel.getpixel((i, j)) & 1 == 1:
                b.append('0b1')
            else:
                b.append('0b0')

    print('save file')
    f = open('output.bin', 'wb')
    b.tofile(f)
    f.close()

if __name__ == '__main__':
    print("Decoding the image...")
    decode_image()

