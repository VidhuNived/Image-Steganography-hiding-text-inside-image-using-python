from PIL import Image

# Creating an Image Object
enc_img = Image.open('encrypted_image.png')

# Loading pixel values of original image, each entry is pixel value ie., RGB values as sublist
enc_pixelMap = enc_img.load()


# Creating an empty String for our hidden message
msg = ""
msg_index = 0 


# Traversing through the pixel values
for row in range(enc_img.size[0]):
    for col in range(enc_img.size[1]):

	# Fetching RGB value a pixel to sublist
        list = enc_pixelMap[row,col]
        r = list[0]	# R value

	if col==0 and row==0:		# 1st pixel was used to store the lenght of message
	    msg_len = r
            
        elif msg_len>msg_index:		# Reading the message from R value of pixel
            msg =msg+ chr(r)		# Converting to character
            msg_index = msg_index+1

enc_img.close()

print "The hidden message is :\n\n"
print msg
                
