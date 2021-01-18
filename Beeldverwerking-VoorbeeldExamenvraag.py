from PIL import Image
import math
import numpy as np

# We definiëren de functie "drawCircle" die de hoogte en breedte van de volledige figuur nodig heeft samen met x,y van het middlepunt van en straal van beide cirkels

def drawCircle(h,w,x1,y1,r1,x2,y2,r2):

    # We maken een nieuwe Image met de PIL Library met de ingegeven breedte en hoogte
    img = Image.new('RGB', (w, h), color = 'grey')

    # Save de afbeelding zodat we deze in de volgende stap kunnen openen
    img.save('test.jpg')

    # Open de afbeelding en converteer ze naar arrays zoals aangegeven in het hoorcollege (deze code tot en met de volgende annotatie is normaal gegeven)
    input_image = Image.open("test.jpg")
    r_image_in, g_image_in, b_image_in = input_image.split()
    r_in = np.uint32(np.array(r_image_in))
    g_in = np.uint32(np.array(g_image_in))
    b_in = np.uint32(np.array(b_image_in))

    # We maken 3 arrays gevuld met nullen met de juiste dimenties zoals te zien is in het hoorcollege
    r_out = np.zeros((r_in.shape[0],r_in.shape[1]))
    g_out = np.zeros((g_in.shape[0],g_in.shape[1]))
    b_out = np.zeros((b_in.shape[0],b_in.shape[1]))

    # We gaan door elk element op elke rij
    for i in range(r_out.shape[0]):

        # We gaan door elk element op elke kolom
        for j in range(r_out.shape[1]):

            # Als het coördinaat (i,j) binnen de straal ligt met middelpunt (x1,y1) moeten we het rood kleuren. We berekenen de lengte tussen het middelpunt en het coördinaat (i,j)
            # met de formule math.sqrt((x2-x1)^2 + (y2-y1)^2)
            if math.sqrt((i-x1)**2 + (j-y1)**2) < r1:
                r_out[i][j] = r_in[i][j]
                g_out[i][j] = 0
                b_out[i][j] = 0
            
            # Als het coördinaat binnen de tweede cirkel ligt (zie methode hierboven) moeten we het groen kleuren.
            if math.sqrt((i-x2)**2 + (j-y2)**2) < r2:
                r_out[i][j] = 0
                g_out[i][j] = g_in[i][j]
                b_out[i][j] = 0
            
            # Als het coördinaat aan beide voldoet en dus op de overlap ligt kleuren we het geel.
            if math.sqrt((i-x1)**2 + (j-y1)**2) < r1 and math.sqrt((i-x2)**2 + (j-y2)**2) < r2:
                r_out[i][j] = r_in[i][j]
                g_out[i][j] = g_in[i][j]
                b_out[i][j] = 0
            
            # Als het coördinaat niet voldoet aan beide cirkels kleuren we het grijs zodat de achtergrond grijs wordt.
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
    

# Vraag de gebruiker naar de benodigde info en roep functie "drawCircle" aan.
heighth = int(input("Input your canvas height: "))
width = int(input("Input your canvas width: "))

x1 = int(input("Input x coordinate of the first circle: "))
y1 = int(input("Input y coordinate of the first circle: "))
r1 = int(input("Input radius of the first circle: ")) 

x2 = int(input("Input x coordinate of the second circle: "))
y2 = int(input("Input y coordinate of the second circle: "))
r2 = int(input("Input radius of the second circle: ")) 

drawCircle(heighth, width, x1,y1,r1,x2,y2,r2)
