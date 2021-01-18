from PIL import Image, ImageDraw
import math
import numpy as np

def drawCircle(h,w,x1,y1,r1,x2,y2,r2):
    img = Image.new('RGB', (w, h), color = 'grey')
    img.save('test.jpg')

    input_image = Image.open("test.jpg")
    r_image_in, g_image_in, b_image_in = input_image.split()
    r_in = np.uint32(np.array(r_image_in))
    g_in = np.uint32(np.array(g_image_in))
    b_in = np.uint32(np.array(b_image_in))

    r_out = np.zeros((r_in.shape[0],r_in.shape[1]))
    g_out = np.zeros((g_in.shape[0],g_in.shape[1]))
    b_out = np.zeros((b_in.shape[0],b_in.shape[1]))

    for i in range(r_out.shape[0]):
        for j in range(r_out.shape[1]):
            if math.sqrt((i-x1)**2 + (j-y1)**2) < r1:
                r_out[i][j] = r_in[i][j]
                g_out[i][j] = 0
                b_out[i][j] = 0
            
            if math.sqrt((i-x2)**2 + (j-y2)**2) < r2:
                r_out[i][j] = 0
                g_out[i][j] = g_in[i][j]
                b_out[i][j] = 0
            
            if math.sqrt((i-x1)**2 + (j-y1)**2) < r1 and math.sqrt((i-x2)**2 + (j-y2)**2) < r2:
                r_out[i][j] = r_in[i][j]
                g_out[i][j] = g_in[i][j]
                b_out[i][j] = 0
            
            elif math.sqrt((i-x1)**2 + (j-y1)**2) > r1 and math.sqrt((i-x2)**2 + (j-y2)**2) > r2:
                average = (r_in[i][j] + g_in[i][j] + b_in[i][j])/3
                r_out[i][j] = average
                g_out[i][j] = average
                b_out[i][j] = average

    r_image_out = Image.fromarray(np.uint8(r_out))
    g_image_out = Image.fromarray(np.uint8(g_out))
    b_image_out = Image.fromarray(np.uint8(b_out))

    output_im = Image.merge("RGB", (r_image_out, g_image_out, b_image_out))
    output_im.show()
    


heighth = int(input("Input your canvas height: "))
width = int(input("Input your canvas width: "))

x1 = int(input("Input x coördinate of the first circle: "))
y1 = int(input("Input y coördinate of the first circle: "))
r1 = int(input("Input radius of the first circle: ")) 

x2 = int(input("Input x coördinate of the second circle: "))
y2 = int(input("Input y coördinate of the second circle: "))
r2 = int(input("Input radius of the second circle: ")) 

drawCircle(heighth, width, x1,y1,r1,x2,y2,r2)
