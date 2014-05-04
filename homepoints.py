import csv
import os

centerpoints = raw_input("What is the name of your homepoint csv file? ")
rawdata = raw_input("What is the name of the csv file containing your GPS data? ")

# erases empty lines and white space from GPS data
def cleandata():

	input = open(rawdata, 'rb')
	output = open('v2'+rawdata, 'wb')
	writer = csv.writer(output)

	for row in csv.reader(input):
		if any(field.strip() for field in row):
			writer.writerow(row)

	input.close()
	output.close()
	os.remove(rawdata)
	os.rename('v2'+rawdata, rawdata)
	
cleandata()

# create 3 lists out from centerpoints - homelat, homelong and radius size in miles
def homepoints():

	with open(centerpoints) as f:
		reader = csv.reader(f)
		global homelatitude
		homelatitude = [col[0] for col in reader]
	with open(centerpoints) as g:
		reader = csv.reader(g)
		global homelongitude
		homelongitude = [col[1] for col in reader]
	with open(centerpoints) as r:
		reader = csv.reader(r)
		global homeradii
		homeradii = [col[2] for col in reader]

homepoints()

# create 2 lists from rawdata - latitude and longitude
def latlong():

	with open(rawdata) as f:
		reader = csv.reader(f)
		global latitude
		latitude = [col[0] for col in reader]
	with open(rawdata) as g:
		reader = csv.reader(g)
		global longitude
		longitude = [col[1] for col in reader]
		
latlong()

# calculates the distance from homelat/long to lat/long and if distance <= radius the data is written into a new csv
def calculate_distance():

	y = 0
	
	for a, b in zip(homelatitude, homelongitude):

		input = open(rawdata, 'rb')
		output = open('final'+rawdata, 'ab')
		writer = csv.writer(output)
		distance = []
		x = 0
	
		for c, d in zip(latitude, longitude):
		
			distance.append(((((float(a) - float(c)) ** 2) * 4761) + (((float(b) - float(d)) ** 2) * 4000)) ** 0.5)
		
		for row in csv.reader(input):
			
			if float(distance[x]) <= float(homeradii[y]):
				writer.writerow(row + [distance[x]])
			else:
				pass
				
			x += 1
				
		y += 1
		
calculate_distance()
	
	
