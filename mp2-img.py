from PIL import Image

im = Image.open("./files/kmimg1.png")

img_arr = [] #container for all the pixel values
pix = im.load() #variable used for containing all the raw pixel values for manipulation

im.show() #print image

#takes the tuples from pix and appends to one-dim array img_arr
for i in range(0, 128):
    for j in range(0, 128):
        # print(pix[i,j])
        img_arr.append(list(pix[i,j]))        

#insert compression code/k-means clustering here

#used to contain the modified pixels in list form
#but they must be in tuple form before reassignment to pix
dest_img = []
for i in range(len(img_arr)):	
	tuple(img_arr)
	dest_img.append(img_arr[i])

# print(dest_img)

#reassignment into pix
for i in range(0, 128):
	for j in range(0, 128):
		pix[i,j] = (0,0,0,255)#tuple(dest_img[i*128+j])



