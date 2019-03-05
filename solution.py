# Import the module (top of the file).
import requests


# Previous code still here.
import geocoder


# Declare destinations list here.

destinations = [
"Space Needle",
"Crater Lake",
"Golden Gate Bridge",
"Yosemite National Park",
"Las Vegas, Nevada",
"Grand Canyon National Park",
"Aspen, Colorado",
"Mount Rushmore",
"Yellowstone National Park",
"Sandpoint, Idaho",
"Banff National Park",
"Capilano Suspension Bridge",
]



for point in destinations:
	# Previous `geopy` code still here.
	g = geocoder.arcgis(point)
	latitude = g.latlng[0]
	longitude = g.latlng[1]

	# Make sure to replace [YOUR_API_KEY_HERE] with your actual key, which
	# will look like a bunch of letters and numbers! Alternatively, copy the sample
	# API call from Dark Sky dashboard and just remove the coordinates.
	API_BASE_URL = "https://api.darksky.net/forecast/041342561deade6845cb7eefea2ef435/"
	
	# full_api_url = API_BASE_URL + latitude + "," + longitude
	full_api_url = API_BASE_URL + str(latitude) + "," + str(longitude)

 
	result = requests.request('GET', full_api_url).json()

	
	print(point, " is located at ", g.latlng)
	#Get the lat-long coordinates from `geocoder.arcgis`.
	#Print out the place name and the coordinates.

	print("At", point, "right now, it's", result["currently"]["summary"], "with a temperature of", result["currently"]["temperature"])
	# From the result, print out the summary and current temperature.

	