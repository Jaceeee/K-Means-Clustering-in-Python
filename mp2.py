import random
import math
import statistics
# constructing the array using list comprehensions
# file_path = '/home/jaceroldan/Documents/3rd Year/Introduction to Artificial Intelligence/Machine Problems/2/Machine Problem 2/kmdata1.txt'
file_path = './files/kmdata1.txt'
output_file_paths = './output/'

file = open(file_path, 'r')

vals = file.readlines()

features = 2
# print(vals)
for i in range(0, len(vals)):
	space_chk = 0
	if vals[i][0] == ' ':
		space_chk = 1
	tmp = vals[i][space_chk : len(vals[i])].split(" ")	
	for j in range(0, features):
		tmp[j] = float(tmp[j])
	vals[i] = (tmp[0], tmp[1])
# print(vals)

minx = min([arr[0] for arr in vals])
maxx = max([arr[0] for arr in vals])
miny = min([arr[1] for arr in vals])
maxy = max([arr[1] for arr in vals])

# print(minx, maxx, miny, maxy, sep=" ")

# print(random.uniform(minx, maxx))
# print(random.uniform(miny, maxy))

centroid = []
k = 3
for i in range(0, k):	
	centroid.append([random.uniform(minx, maxx), random.uniform(miny, maxy)])

# print(centroid)

#stores all the differences in one 2D array
inp = int(input("Enter a number: "))
n = inp
cost = 0
while n > 0:
	dj = cost
	differences_array = []

	for i in range(0, len(vals)):
		differences = []
		for j in range(0, k):
			sum = 0
			for l in range(0, features):
				sum = sum + ((vals[i][l] - centroid[j][l]) ** 2)
			sum = math.sqrt(sum)
			differences.append(sum)
		differences_array.append(differences)

	# reduces the differences array into a matrix of differences
	# uses the assignment array to indicate which cluster it belongs to
	# print(differences_array)
	assignment = []
	for i in range(0, len(vals)):		
		assignment.append(differences_array[i].index(min(differences_array[i])))
		differences_array[i] = min(differences_array[i])
	
	# print(assignment)
	output_file_ca = open(output_file_paths+'iter'+str(10-n+1)+'_ca.txt', 'w+')	
	to_file_output_assignment = ''.join((str(e)+'\n') for e in assignment)	
	# print(output_assignment)
	output_file_ca.write(to_file_output_assignment)
	output_file_ca.close()

	means_array = []
	for i in range(0, k):
		means_array.append([])

	# change centroid step
	print("iteration ", 10-n+1, ":", sep="")
	# print("before... ", centroid)
	for i in range(0, k):			#for each centroid value		    
	    for j in range(0, features): #going through each feature
	        sum_arr = []  #set a sum array	        
	        for l in range(0, len(vals)): #going through each point
	            ind = assignment[l];
	            if ind == i:	# if it matches the centroid's designation
	                sum_arr.append(vals[l][j])  #append that value to the sum_arr                
	        if len(sum_arr) > 0:
	        	centroid[i][j] = statistics.mean(sum_arr)

	# print("after...  ", centroid)
	#TODO insert file writing of centroid locations into "iter<n>_cm.txt"	
	output_file_cm = open(output_file_paths+'iter'+str(10-n+1)+'_cm.txt', 'w+')
	to_file_output_centroid = ''

	for i in range(0, len(centroid)):
	    to_file_output_centroid = to_file_output_centroid + '(' + ''.join((str(e) + ', ') for e in centroid[i]) + '\b\b)' + '\n'	    
	    # print(centroid[i])	    


	# to_file_output_centroid = ''.join(((str(e) + ' ') for e in ordered_pair) for ordered_pair in centroid)
	#TODO insert file appending J, value of distortion function, into "iter<n>_cm.txt"
	#TODO insert file appending dJ, value of the difference of the current J from the previous J, into "iter<n>_cm.txt"	

	cost =  statistics.mean(differences_array)	
	dj = 0 if n == inp else dj - cost
	
	to_file_output_centroid = to_file_output_centroid + str(cost) + '\n' + str(dj)

	print(to_file_output_centroid)
	output_file_cm.close()
	n -= 1