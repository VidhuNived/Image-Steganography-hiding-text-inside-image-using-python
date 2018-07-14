# Steganography-hiding-text-inside-image-using-python
# Steganography
Steganography is the hiding of a secret message within an ordinary message and the extraction of it at its destination. Here we use an image to hide the textual message.

The encoding of the secret content is performed using the well acknowledged encryption algorithm, LSB encoding, which is to perform mainpuation to LSB values of the byte, which in this case is the pixel value R,G and B.

First pixels R value is used to store the lenght of message, the following pixels are used to store the message itself.

JPEG images cannot be used for carrying the message because the hidden content inthe LSB of the image will be lost during compression, thus we must go for some other formats like PNG, where these issue doesnot exist.

The pograms Encoder and Decoder are used to encode and decode secret image into carrier image. Both communicating parties must have the same pair if encoder and decoder program inorder to function properly.


REQUIREMENTS

PIL package of python is neccessay to run the program. The instruction to install PIL is given below:

--->>> pip install pillow

pip is python package installer, it must be install first although its preinstalled in many Linux Distributions.

--->>> sudo apt-get install python-pip


orginal_image is the carrier image.

encrypted_image is the carrier image with hidden data, also this is the image which we transmit via network.


Here program encoder is ran, and the user is asked enter the message that is to be transmitted and at reciver's end decoder program will print the hidden message to the user's terminal. 
