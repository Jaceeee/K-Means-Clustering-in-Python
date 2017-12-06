from PIL import Image
import random
import math
import statistics

im = Image.open("./files/kmimg1.png")
features = 3
k = 16
MAX = 16384

img_arr = [] #container for all the pixel values
pix = im.load() #variable used for containing all the raw pixel values for manipulation

im.show() #print original image

#takes the tuples from pix and appends to one-dim array img_arr
for i in range(0, 128):
    for j in range(0, 128):
        # print(pix[i,j])
        img_arr.append(list(pix[i,j]))        

for i in range(0, 16384):
	for j in range(0, features):
		img_arr[i][j] = int(img_arr[i][j])
#insert compression code/k-means clustering here

#used to contain the modified pixels in list form
#but they must be in tuple form before reassignment to pix

dest_img = []
for i in range(len(img_arr)):
	dest_img.append(tuple(img_arr[i]))

centroid = []

for i in range(0, k):
	centroid.append(img_arr[random.randint(0, 16384)])

inp = 10
n = inp

while n > 0:
	differences_array = []

	for i in range(0, len(img_arr)):
		differences = []
		for j in range(0, k):
			sum = 0
			for l in range(0, features):
				sum = sum + ((img_arr[i][l] - centroid[j][l]) ** 2)
			sum = math.sqrt(sum)
			differences.append(sum)
		differences_array.append(differences)

	# reduces the differences array into a matrix of differences
	# uses the assignment array to indicate which cluster it belongs to 
	# the index of differences array in that particular iteration will then be reduced to a single value
	# print(differences_array)
	assignment = []
	for i in range(0, len(img_arr)):
		assignment.append(differences_array[i].index(min(differences_array[i])))
		differences_array[i] = min(differences_array[i])

	#print(assignment)

	means_array = []
	for i in range(0, k):
		means_array.append([])

	# change centroid step
	# print("iteration ", 10 - n + 1, ":", sep="")
	# print("before... ", centroid)
	for i in range(0, k):
		for j in range(0, features):
			sum_arr = []
			for l in range(0, len(img_arr)):
				ind = assignment[l]
				if ind == i:
					sum_arr.append(img_arr[l][j])
			if len(sum_arr) > 0:
				centroid[i][j] = statistics.mean(sum_arr)

	# print("after... ", centroid)

	n -= 1

# compress the image by assigning the new intensity values
# of centroids
for i in range(0, MAX):
	dest_img[i] = ([int(e) for e in centroid[assignment[i]] ])

# print(dest_img)

#reassignment into pix
for i in range(0, 128):
	for j in range(0, 128):
		print("it = ",i*128+j,": ", dest_img[i*128+j])
		pix[i,j] = tuple(dest_img[i*128+j])

im.save('./output_comp/output.png')
im.show() #print modified image