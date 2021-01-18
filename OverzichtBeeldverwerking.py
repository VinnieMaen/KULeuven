from PIL import Image
import math
import numpy as np

input_image = Image.open("test.jpg")
r_image_in, g_image_in, b_image_in = input_image.split()
r_in = np.uint32(np.array(r_image_in))
g_in = np.uint32(np.array(g_image_in))
b_in = np.uint32(np.array(b_image_in))


# Voor alle bewerkingen buiten rotatie

r_out = np.zeros((r_in.shape[0],r_in.shape[1]))
g_out = np.zeros((g_in.shape[0],g_in.shape[1]))
b_out = np.zeros((b_in.shape[0],b_in.shape[1]))


# Wijziging voor rotatie 90 graden *

r_out = np.zeros((r_in.shape[1],r_in.shape[0]))
g_out = np.zeros((g_in.shape[1],g_in.shape[0]))
b_out = np.zeros((b_in.shape[1],b_in.shape[0]))


# Herschaleren van de afbeelding (hoogte neemt af met 100px)

r_out = np.zeros((r_in.shape[0] - 100,r_in.shape[1]))
g_out = np.zeros((g_in.shape[0] - 100,g_in.shape[1]))
b_out = np.zeros((b_in.shape[0] - 100,b_in.shape[1]))


# Herschaleren van de afbeelding (breedte neemt af met 100px)

r_out = np.zeros((r_in.shape[0],r_in.shape[1] - 100))
g_out = np.zeros((g_in.shape[0],g_in.shape[1] - 100))
b_out = np.zeros((b_in.shape[0],b_in.shape[1] - 100))

for i in range(r_out.shape[0]):
    for j in range(r_out.shape[1]):

        # Kleuren rood en blauw wegdoen

        r_out[i][j] = 0
        g_out[i][j] = g_in[i][j]
        b_out[i][j] = 0


        # Negatieve kleuren
         
        r_out[i][j] = 255-r_in[i][j]
        g_out[i][j] = 255-g_in[i][j]
        b_out[i][j] = 255-b_in[i][j]


        # Grijswaarden van de afbeelding

        av = (r_in[i][j] + g_in[i][j] + b_in[i][j])/3
        r_out[i][j] = av
        g_out[i][j] = av
        b_out[i][j] = av


        # Afbeelding donkerder maken met factor 5

        r_out[i][j] = r_in[i][j]/5
        g_out[i][j] = g_in[i][j]/5
        b_out[i][j] = b_in[i][j]/5
        

        # Afbeelding verhelderen met factor 5
        r_out[i][j] = (255-r_in[i][j])/5 + r_in[i][j]
        g_out[i][j] = (255-g_in[i][j])/5 + g_in[i][j]
        b_out[i][j] = (255-b_in[i][j])/5 + b_in[i][j]


        # Roteren van de afbeelding over 90 graden (zie wijziging boven for loops *)

        r_out[i][j] = r_in[r_in.shape[0]-j-1][i]
        g_out[i][j] = g_in[r_in.shape[0]-j-1][i]
        b_out[i][j] = b_in[r_in.shape[0]-j-1][i]
        

        # Horizontaal spiegelen

        r_out[i][j] = r_in[r_in.shape[0]-i-1][j]
        g_out[i][j] = g_in[r_in.shape[0]-i-1][j]
        b_out[i][j] = b_in[r_in.shape[0]-i-1][j]


        # Verticaal spiegelen

        r_out[i][j] = r_in[i][r_in.shape[1]-j-1]
        g_out[i][j] = g_in[i][r_in.shape[1]-j-1]
        b_out[i][j] = b_in[i][r_in.shape[1]-j-1]

r_image_out = Image.fromarray(np.uint8(r_out))
g_image_out = Image.fromarray(np.uint8(g_out))
b_image_out = Image.fromarray(np.uint8(b_out))

output_im = Image.merge("RGB", (r_image_out, g_image_out, b_image_out))
output_im.show()
