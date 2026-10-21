#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  Oktober 19_21 2026 - LAB 1                                                                
#             Today's study goal is: API - Guided practice                                  *
#********************************************************************************************


#############################################################################################
#********************************************************************************************
#  LAB 1.1  - Task 1  Guided practice                                                         *
#********************************************************************************************

# In this lab you practise what we did in the lecture, on the same API: https://fakestoreapi.com
# (open, no key). You will fetch data, sort and filter it, move your get_json function into its own
# file, and write to the API. Use the get_json function from the morning. Remember that it is a
# fake API, so POST, PATCH and DELETE are not really saved.

# Endpoints you need
# GET /products
# GET /products/categories
# GET /products/category/<name>
# POST /products
# PATCH /products/<id>

#########################
#       Tasks:
######################

#******************************************************************************************
# LAB 1.1.1 Sort the products by price
#--------------------------------
# Fetch /products with get_json. You get a list of dictionaries. Sort the list so the
# cheapest product comes first and print one line per product with the price and the title.
# Hint: sorted(products, key=...), where the key function takes one product and
# returns its price.
#******************************************************************************************


# import requests

# def get_json(url):
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json()


# # Fetch products from the API
# url = "https://fakestoreapi.com/products"
# products = get_json(url)

# # Sort products by price (cheapest first)
# sorted_products = sorted(products, key=lambda product: product["price"])

# # Print one line per product with price and title
# print("--- PRODUCTS SORTED BY PRICE (ASCENDING) ---")
# for product in sorted_products:
#     print(f"{product['price']} kr - {product['title']}")

# Terminal:
#        7.95 kr - Opna Women's Short Sleeve Moisture
#        9.85 kr - MBJ Women's Solid Short Sleeve Boat Neck V 
#        9.99 kr - White Gold Plated Princess
#       10.99 kr - Pierced Owl Rose Gold Plated Stainless Steel Double
#       12.99 kr - DANVOUY Womens T Shirt Casual Cotton Short
#       15.99 kr - Mens Casual Slim Fit
#       22.3 kr - Mens Casual Premium Slim Fit T-Shirts 
#       29.95 kr - Lock and Love Women's Removable Hooded Faux Leather Moto Biker Jacket
#       39.99 kr - Rain Jacket Women Windbreaker Striped Climbing Raincoats
#       55.99 kr - Mens Cotton Jacket
#       56.99 kr - BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats
#       64 kr - WD 2TB Elements Portable External Hard Drive - USB 3.0 
#       109 kr - SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s
#       109 kr - Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5
#       109.95 kr - Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops
#       114 kr - WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive
#       168 kr - Solid Gold Petite Micropave 
#       599 kr - Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin
#       695 kr - John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet
#       999.99 kr - Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED 
#------------------------------------------------------------------------------------------------


#****************************************************************************************
# LAB 1.1.2 Look at the categories
#-------------------------
# 2.1. Fetch /products/categories and print the result. 
# 2.2. Then ask the user to type one of the categories with input(). 
# 2.3. Fetch /products/category/<name> and 
# 2.4 print how many # products it has and which one is the cheapest. 
# 2.5 Think about what happens if the user
# types a category that does not exist. Note: the category is spelled jewelery in this API.
# That is not your mistake.
#******************************************************************************************


# import requests

# def get_json(url):
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json()


# # 2.1. Fetch and print all categories
#-----------------------------------------
# base_url = "https://fakestoreapi.com"
# categories = get_json(f"{base_url}/products/categories")

# # print("Available categories:")
# # for cat in categories:
# #     print(f"- {cat}")

# # # Available categories:
# # # - electronics
# # # - jewelery
# # # - men's clothing
# # # - women's clothing


# # 2.2. Ask the user to enter a category
#----------------------------------------
# user_choice = input(
#     "\nEnter a category name: "
# ).strip()  # Note: API spells it 'jewelery'

# # Terminal:Enter a category name: electronics

# if user_choice not in categories:
#     print(
#         f"Error: '{user_choice}' is not a valid category. Please run again and pick from the list above."
#     )
# else:
# #2.3. Fetch products for the chosen category
#-----------------------------------------------
#     category_products = get_json(f"{base_url}/products/category/{user_choice}")

# # 2.4. Print count and cheapest product
#-------------------------------------------
#     if category_products:
#         print(
#             f"\nCategory '{user_choice}' has {len(category_products)} products."
#         )

#         cheapest = min(category_products, key=lambda p: p["price"])
#         print(
#             f"Cheapest product: {cheapest['title']} ({cheapest['price']} kr)"
#         )
#     else:
#         print("No products found in this category.")


# # Terminal:   Category 'electronics' has 6 products.
# #             Cheapest product: WD 2TB Elements Portable External Hard Drive - USB 3.0  (64 kr)

#2.5 Enter a category name: Accessories
#------------------------------------------
#    Error: 'Accessories' is not a valid category. Please run again and pick from the list above.
#----------------------------------------------------------------------------


#*****************************************************************************
# LAB 1.1.3.  Move get_json to its own file
#----------------------------------------------------------------------
# 3.1. Create a file called api_client.py and move the get_json function there. 
# 3.2. In your lab file, import it with from api_client import get_json. 
# Run the lab again. 
# It should work exactly as before. You will reuse this file in Lab 2.
#******************************************************************************

# # 3.2.
# from api_client import get_json


# products = get_json("https://fakestoreapi.com/products")
# sorted_products = sorted(products, key=lambda p: p["price"])

# print("--- CHEAPEST PRODUCT ---")
# print(f"{sorted_products[0]['price']} kr - {sorted_products[0]['title']}")

# # 
# categories = get_json("https://fakestoreapi.com/products/categories")
# print("\nAvailable categories:", categories)

# # Terminal: --- CHEAPEST PRODUCT ---
# #           7.95 kr - Opna Women's Short Sleeve Moisture

# #           Available categories: ['electronics', 'jewelery', "men's clothing", "women's clothing"]
#----------------------------------------------------------------------------



#********************************************************************************************
# LAB1.1.4 Create and change a product
#-------------------------------------
# Build a dictionary for a new product (title, price, description, image, category, but no id).
# Send it with requests.post(..., json=...) and print the status code and the answer.
# Then change the price of an existing product, for example product 7, with
# requests.patch and a body that only contains the price. Print the answer. get_json
# only does GET, so here you call requests directly. Remember the timeout and check the
# status code.
#**********************************************************************************************


# import requests

# BASE_URL = "https://fakestoreapi.com/products"
# TIMEOUT = 10  # Seconds timeout for network requests

# # --- 1. CREATE A NEW PRODUCT (POST) ---
# new_product = {
#     "title": "Powers best laptop",
#     "price": 84999.00,
#     "description": "Lenovo Yoga Pro 9 15N1X (N1X/128/2TB) NVIDIA RTX Spark™ N1X 15” bärbar dator    .",
#     "image": "https://www.power.se/datorer-och-surfplattor/datorer/barbar-dator/lenovo-yoga-pro-9-15n1x-n1x1282tb-nvidia-rtx-spark-n1x-15-barbar-dator/p-4310215/",
#     "category": "electronics",
# }

# print("--- POST /products ---")
# try:
#     response = requests.post(BASE_URL, json=new_product, timeout=TIMEOUT)
#     print(f"Status Code: {response.status_code}")

#     if response.status_code == 200 or response.status_code == 201:
#         print("Response JSON:", response.json())
#     else:
#         print("Failed to create product:", response.text)
# except requests.exceptions.RequestException as e:
#     print(f"Request failed: {e}")

# print("\n" + "-" * 30 + "\n")

# # Terminal: 
#     # --- POST /products ---
#     # Status Code: 201
#     # Response JSON: {'id': 21, 'title': 'Powers best laptop', 'price': 84999, 
#     # 'description': 'Lenovo Yoga Pro 9 15N1X (N1X/128/2TB) NVIDIA RTX Spark™ N1X 15” bärbar dator    .', 
#     # 'image': 'https://www.power.se/datorer-och-surfplattor/datorer/barbar-dator/lenovo-yoga-pro-9-15n1x-n1x1282tb-nvidia-rtx-spark-n1x-15-barbar-dator/p-4310215/', 'category': 'electronics'}



# # --- 2. UPDATE AN EXISTING PRODUCT PRICE (PATCH) ---
# product_id = 7
# patch_data = {"price": 74999.00}

# print(f"--- PATCH /products/{product_id} ---")
# try:
#     response = requests.patch(
#         f"{BASE_URL}/{product_id}", json=patch_data, timeout=TIMEOUT
#     )
#     print(f"Status Code: {response.status_code}")

#     if response.status_code == 200:
#         print("Response JSON:", response.json())
#     else:
#         print("Failed to patch product:", response.text)
# except requests.exceptions.RequestException as e:
#     print(f"Request failed: {e}")


# # Terminal: 
#     # Status Code: 200
#     # Response JSON: {'id': 7, 'price': 74999}



#******************************************************************************************
# LAB 1.1.5 Break it on purpose
#------------------------------
# Call your function with a wrong URL, with timeout=0.001, and with a made-up domain.
# For each one, read the message you get. The program must not crash, and every
# problem should give a short message that a human can read.
#
# Expected for task 4: status 200 and an answer with an id (the fake API answers 200, a real
# API often answers 201). For PATCH the fake API just sends back what you sent.
#*******************************************************************************************

# import requests
# from api_client import get_json

# # --- 1. Wrong URL (404 Not Found) ---
# print("--- Test 1: Wrong URL ---")
# try:
#     data = get_json("https://fakestoreapi.com/non_existent_endpoint_12345")
# except requests.exceptions.HTTPError as e:
#     print(
#         f"Error: The requested page/endpoint was not found. ({e.response.status_code})"
#     )
# except requests.exceptions.RequestException as e:
#     print(f"Request failed: {e}")

# print("\n" + "-" * 40 + "\n")

# # Terminal:
#     # --- Test 1: Wrong URL ---
#     # Error: The requested page/endpoint was not found. (404)

#     # ----------------------------------------


# # --- 2. Timeout Too Short (Timeout Error) ---
# print("--- Test 2: Timeout = 0.001s ---")
# try:
#     response = requests.get(
#         "https://fakestoreapi.com/products", timeout=0.001
#     )
#     response.raise_for_status()
# except requests.exceptions.Timeout:
#     print("Error: The request timed out because the server took too long to respond.")
# except requests.exceptions.RequestException as e:
#     print(f"Request failed: {e}")

# print("\n" + "-" * 40 + "\n")


# # Terminal:
#     # --- Test 2: Timeout = 0.001s ---
#     # Error: The request timed out because the server took too long to respond.

#     # ----------------------------------------


# # --- 3. Made-up Domain (DNS / Connection Error) ---
# print("--- Test 3: Made-up Domain ---")
# try:
#     data = get_json("https://this-domain-definitely-does-not-exist-99999.com")
# except requests.exceptions.ConnectionError:
#     print("Error: Could not connect to the server. Check the domain name or network connection.")
# except requests.exceptions.RequestException as e:
#     print(f"Request failed: {e}")

# # Terminal: 
#     # --- Test 3: Made-up Domain ---
#     # Error: Could not connect to the server. Check the domain name or network connection.




#############################################################################################
#********************************************************************************************
#  LAB 1.2  - Task/LAB 2: Your own tool                                                         *
#
# In this lab you build a small tool of your own. The user types the name of a city, and the
# program prints the current temperature and wind speed. You use Open-Meteo, which is open
# and needs no key.
# The weather API does not understand city names. It wants coordinates. So the tool needs two
# requests after each other:
#********************************************************************************************

# Step      What happens                                You get
# 1         Ask the user for a city                     A city name, e.g. Stockholm
# 2         Geocoding API: city name to coordinates     latitude and longitude
# 3         Forecast API: coordinates to weather        temperature and wind speed, then print


# # 1. City name -> coordinates
# https://geocoding-api.open-meteo.com/v1/search
# params: name=Stockholm, count=1
# # 2. Coordinates -> weather
# https://api.open-meteo.com/v1/forecast
# params: latitude, longitude,
# current=temperature_2m,wind_speed_10m


# TASK: 

##################################################################################################
#**************************************
# LAB 1.2.1 Find the coordinates of a city
#*************************************
# Call the geocoding endpoint with get_json and the params name and count=1. 
# - Print the whole answer first and look at it before you pick out values. 
# You will see a dictionary with a key results, which is a list. 
# The first item in that list is your city, with the name, the country, the latitude and the longitude. 
# - Then print only the latitude and the longitude.
#*****************************************************************************************

# from api_client import get_json

# Geocoding_URL = "https://geocoding-api.open-meteo.com/v1/search"

# city_name = input("Enter a city name (e.g., Stockholm): ").strip()

# params = {
#     "name": city_name,
#     "count": 1
# }

# Terminal:
    # 1. Enter a city name (e.g., Stockholm): Belgrade

    # --- RAW API RESPONSE ---
    # {'results': [{'id': 792680, 'name': 'Belgrade', 'latitude': 44.80401, 'longitude': 20.46513, 
    # 'elevation': 120.0, 'feature_code': 'PPLC', 'country_code': 'RS', 'admin1_id': 785958, 
    # 'admin2_id': 8199669, 'timezone': 'Europe/Belgrade', 'population': 1273651, 
    # 'country_id': 6290252, 'country': 'Serbia', 'admin1': 'Central Serbia', 'admin2': 'Belgrade'}],
    #  'generationtime_ms': 0.14138222}


    # 2. Enter a city name (e.g., Stockholm): Smederevska Palanka

    # --- RAW API RESPONSE ---
    # {'results': [{'id': 785753, 'name': 'Smederevska Palanka', 'latitude': 44.36548, 'longitude': 20.95885, 
    # 'elevation': 119.0, 'feature_code': 'PPLA3', 'country_code': 'RS', 'admin1_id': 785958, 
    # 'admin2_id': 7581804, 'admin3_id': 785752, 'timezone': 'Europe/Belgrade', 'population': 27000, 
    # 'country_id': 6290252, 'country': 'Serbia', 'admin1': 'Central Serbia', 'admin2': 'Podunavlje', 
    # 'admin3': 'Opština Smederevska Palanka'}],  'generationtime_ms': 0.059127808}


    # 3. Enter a city name (e.g., Stockholm): Donja Livadica

    # --- RAW API RESPONSE ---
    # {'results': [{'id': 791286, 'name': 'Donja Livadica', 'latitude': 44.35444, 'longitude': 21.14356,
    # 'elevation': 90.0, 'feature_code': 'PPL', 'country_code': 'RS', 'admin1_id': 785958, 'admin2_id': 7581804, 
    # 'admin3_id': 784629, 'timezone': 'Europe/Belgrade', 'country_id': 6290252, 'country': 'Serbia', 'admin1': 'Central Serbia',
    #  'admin2': 'Podunavlje', 'admin3': 'Opština Velika Plana'}], 'generationtime_ms': 0.12743473}



# Construct URL with query parameters and fetch data
# URL becomes: https://geocoding-api.open-meteo.com/v1/search?name=Stockholm&count=1

# data = get_json(f"{Geocoding_URL}?name={params['name']}&count={params['count']}")

# # 1.  Print the whole answer first
# print("\n--- RAW API RESPONSE ---")
# print(data)

# # Extract and print specific coordinates safely
# if data and "results" in data and len(data["results"]) > 0:
#     city_info = data["results"][0]
    
#     name = city_info.get("name")
#     country = city_info.get("country", "Unknown country")
#     lat = city_info.get("latitude")
#     lon = city_info.get("longitude")
    
#     print("\n--- EXTRACTED COORDINATES ---")
#     print(f"City: {name}, {country}")
#     print(f"Latitude: {lat}")
#     print(f"Longitude: {lon}")
# else:
#     print(f"\nCould not find any coordinates for '{city_name}'.")


# Terminal:

    # 1. Enter a city name (e.g., Stockholm): Belgrade
    # --- EXTRACTED COORDINATES ---
    # City: Belgrade, Serbia
    # Latitude: 4480401
    # Longitude: 20.46513
#******************************************************************************************




#*************************************************************************************
# LAB 1.2.2 Get the weather for those coordinates
#---------------------------------------------------------
# Call the forecast endpoint with the params latitude, longitude and current set to
# temperature_2m,wind_speed_10m. 1. Print the whole answer first. 
# You will find a key current with the values you want, and a key current_units that tells you the units.
#**********************************************************************************

# from api_client import get_json

# GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
# FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# city_name = input("Enter a city name (e.g., Stockholm): ").strip()

# geo_data = get_json(f"{GEOCODING_URL}?name={city_name}&count=1")

# if geo_data and "results" in geo_data and len(geo_data["results"]) > 0:
#     city_info = geo_data["results"][0]
#     lat = city_info["latitude"]
#     long = city_info["longitude"]
#     found_city = city_info["name"]
#     country = city_info.get("country", "")

#     print(f"\nFound location: {found_city}, {country} (Lat: {lat}, Lon: {long})")

# # Terminal: 
#     # Enter a city name (e.g., Stockholm): Belgrade
#     # Found location: Belgrade, Serbia (Lat: 44.80401, Lon: 20.46513)


#     # Get current weather via Forecast API using the extracted coordinates
#     forecast_endpoint = (
#         f"{FORECAST_URL}?latitude={lat}&longitude={long}"
#         "&current=temperature_2m,wind_speed_10m"
#     )

#     weather_data = get_json(forecast_endpoint)

#     # Print raw response first as requested
#     print("\n--- RAW FORECAST API RESPONSE ---")
#     print(weather_data)

#     # Extract current weather and units
#     if weather_data and "current" in weather_data:
#         current = weather_data["current"]
#         units = weather_data.get("current_units", {})

#         temp = current.get("temperature_2m")
#         temp_unit = units.get("temperature_2m", "°C")

#         wind = current.get("wind_speed_10m")
#         wind_unit = units.get("wind_speed_10m", "km/h")

#         print("\n--- CURRENT WEATHER ---")
#         print(f"Temperature: {temp} {temp_unit}")
#         print(f"Wind Speed:  {wind} {wind_unit}")
#     else:
#         print("Could not retrieve current weather data.")

# else:
#     print(f"City '{city_name}' not found.")

# Terminal:
    # Enter a city name (e.g., Stockholm): Belgrade

    # Found location: Belgrade, Serbia (Lat: 44.80401, Lon: 20.46513)

    # --- RAW FORECAST API RESPONSE ---
    # {'latitude': 44.810673, 'longitude': 20.458527, 'generationtime_ms': 0.029087066650390625, 'utc_offset_seconds': 0, 
    # 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 120.0, 
    # 'current_units': {'time': 'iso8601', 'interval': 'seconds', 'temperature_2m': '°C', 'wind_speed_10m': 'km/h'}, 
    # 'current': {'time': '2026-10-21T07:45', 'interval': 900, 'temperature_2m': 17.1, 'wind_speed_10m': 23.8}}

    # --- CURRENT WEATHER ---
    # Temperature: 17.1 °C
    # Wind Speed:  23.8 km/h


#**************************************************************************
# LAB 1.2.3 Put it together
#--------------------------
# Ask the user for a city with input(). Use the answer from step 1 for the coordinates, 
# and then call the forecast. Print one line like this (numbers will differ): 
# Stockholm, Sweden: 8.4°C, wind 12.3 km/h. 
# Tip: put each of the two requests in its own function, for example find_city(name) and get_weather(lat, lon).
#****************************************************************************************************************

# from api_client import get_json

# GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
# FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


# def find_city(name: str) -> dict | None:
#     """Fetches coordinates and metadata for a given city name."""
#     url = f"{GEOCODING_URL}?name={name}&count=1"
#     data = get_json(url)

#     if data and "results" in data and len(data["results"]) > 0:
#         first_result = data["results"][0]
#         return {
#             "name": first_result.get("name"),
#             "country": first_result.get("country", ""),
#             "latitude": first_result.get("latitude"),
#             "longitude": first_result.get("longitude"),
#         }
#     return None


# def get_weather(lat: float, lon: float) -> dict | None:
#     """Fetches current weather readings given latitude and longitude."""
#     url = f"{FORECAST_URL}?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
#     data = get_json(url)

#     if data and "current" in data:
#         current = data["current"]
#         units = data.get("current_units", {})
#         return {
#             "temp": current.get("temperature_2m"),
#             "temp_unit": units.get("temperature_2m", "°C"),
#             "wind": current.get("wind_speed_10m"),
#             "wind_unit": units.get("wind_speed_10m", "km/h"),
#         }
#     return None


# def main():
#     city_input = input("Enter a city name: ").strip()
#     if not city_input:
#         print("Please enter a valid city name.")
#         return

#     # Geocode city name to coordinates
#     location = find_city(city_input)
#     if not location:
#         print(f"City '{city_input}' was not found.")
#         return

#     # Fetch weather for retrieved coordinates
#     weather = get_weather(location["latitude"], location["longitude"])
#     if not weather:
#         print("Could not retrieve weather data at this time.")
#         return

#     # Format single-line output
#     country_str = f", {location['country']}" if location["country"] else ""
#     print(
#         f"{location['name']}{country_str}: "
#         f"{weather['temp']}{weather['temp_unit']}, "
#         f"wind {weather['wind']} {weather['wind_unit']}"
#     )


# if __name__ == "__main__":
#     main()

# Terminal:

    # Enter a city name: Belgrade
    # Belgrade, Serbia: 17.6°C, wind 23.8 km/h


#************************************************************************************
# LAB 1.2.4 Handle a city that does not exist
#--------------------------------------------
# What happens if the user types a city that does not exist? Handle it so the program
# prints a message and does not crash. Hint: print the answer for a city that does not
# exist, for example asdfghjkl, and look at what is different compared with a city that
# does exist.
#**************************************************************************************


# from api_client import get_json

# GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
# FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


# def find_city(name: str) -> dict | None:
#     """
#     Fetches coordinates for a given city name.
#     Returns None if the city does not exist or has no matching results.
#     """
#     url = f"{GEOCODING_URL}?name={name}&count=1"
#     data = get_json(url)

#     # Key Check: If city does not exist, 'results' is either missing or empty/None
#     if not data or "results" not in data or not data["results"]:
#         return None

#     first_result = data["results"][0]
#     return {
#         "name": first_result.get("name"),
#         "country": first_result.get("country", ""),
#         "latitude": first_result.get("latitude"),
#         "longitude": first_result.get("longitude"),
#     }


# def get_weather(lat: float, lon: float) -> dict | None:
#     """Fetches current weather readings given latitude and longitude."""
#     url = f"{FORECAST_URL}?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
#     data = get_json(url)

#     if not data or "current" not in data:
#         return None

#     current = data["current"]
#     units = data.get("current_units", {})

#     return {
#         "temp": current.get("temperature_2m"),
#         "temp_unit": units.get("temperature_2m", "°C"),
#         "wind": current.get("wind_speed_10m"),
#         "wind_unit": units.get("wind_speed_10m", "km/h"),
#     }


# def main():
#     city_input = input("Enter a city name: ").strip()
#     if not city_input:
#         print("Please enter a valid city name.")
#         return

#     # Look up city coordinates
#     location = find_city(city_input)

#     # Handle non-existent city gracefully
#     if location is None:
#         print(f"Error: Could not find any city named '{city_input}'. Please check spelling and try again.")
#         return

#     # Fetch weather if city was found
#     weather = get_weather(location["latitude"], location["longitude"])
#     if weather is None:
#         print("Error: Could not retrieve weather data at this time.")
#         return

#     # Format single-line output
#     country_str = f", {location['country']}" if location["country"] else ""
#     print(
#         f"{location['name']}{country_str}: "
#         f"{weather['temp']}{weather['temp_unit']}, "
#         f"wind {weather['wind']} {weather['wind_unit']}"
#     )


# if __name__ == "__main__":
#     main()


# Terminal: 
    # Enter a city name: Vaxholm
    # Vaxholm, Sweden: 10.6°C, wind 19.4 km/h
#***************************************************************************************


###############################################################################################
#********************************************************************************************
#  LAB 1.3  - Task/Lab 3: Authentication and secrets
#
# In this lab you call an API with a token, so the API knows who you are, and you keep that token
# out of your code and out of Git. You use the GitHub API to print the 5 latest pushed repositories
# of a user. Without a token GitHub allows 60 requests per hour, with a token 5000.                                                    *
#********************************************************************************************


# Endpoint you need
# GET https://api.github.com/users/<username>/repos
# params: sort=pushed, per_page=5
# header: Authorization: Bearer <token>


# Tasks

#*******************************************************************************************
# LAB 1.3.1 Create a token
#-------------------------
# Log in to github.com. Click your profile picture, choose Settings, scroll down in the left
# menu and click Developer settings. Choose Personal access tokens, then Tokens
# (classic), then Generate new token (classic). Name it api-course and pick a short
# expiry, for example 7 days. Do not tick any scopes, because we only read public
# information. Click Generate token and copy it right away. GitHub shows it only once.
# (GitHub sometimes renames menus. If something does not match, look for the names inbold.)
#******************************************************************************************


# DONE: I have saved the token on a secret lokation.


#*******************************************************************************************
# LAB 1.3.2 Store it safely
#-------------------------
# In a new folder, create .gitignore first and put .env in it. Then create .env and write
# GITHUB_TOKEN=your_token in it, with no quotes. Do not paste the token in chat, do not
# take a screenshot of it, and do not share your screen while it is visible.
#******************************************************************************************


# Done



#*******************************************************************************************
# LAB 1.3.3 Call the API with the token
#--------------------------------------
# Load the token with load_dotenv() and os.getenv("GITHUB_TOKEN"). Send it in the
# header Authorization: Bearer <token>. Ask for a GitHub username with input(),
# call the endpoint above, and print the name of each repository. Use get_json from
# api_client.py.
#******************************************************************************************


# import os
# from dotenv import load_dotenv
# from api_client import get_json

# # Load environment variables from .env file
# load_dotenv()

# # Retrieve GITHUB_TOKEN from the environment
# token = os.getenv("GITHUB_TOKEN")

# if not token:
#     print("Error: GITHUB_TOKEN not found in .env file.")
#     exit(1)

# username = input("Enter a GitHub username: ").strip()

# if not username:
#     print("Error: Username cannot be empty.")
#     exit(1)

# # Define API endpoint and authentication headers
# url = f"https://api.github.com/users/{username}/repos?sort=pushed&per_page=5"
# headers = {
#     "Authorization": f"Bearer {token}",
#     "Accept": "application/vnd.github+json"
# }

# # Make the API call and display repository names
# try:
#     repos = get_json(url, headers=headers)

#     print(f"\n--- Top 5 latest pushed repositories for '{username}' ---")
#     if isinstance(repos, list) and len(repos) > 0:
#         for repo in repos:
#             print(f"- {repo['name']}")
#     else:
#         print("No public repositories found for this user.")

# except Exception as e:
#     print(f"Failed to fetch repositories: {e}")


# # Terminal: 
    
#     #  1.   Enter a GitHub username: octocat

#     # --- Top 5 latest pushed repositories for 'octocat' ---
#     # - Spoon-Knife
#     # - Hello-World
#     # - linguist
#     # - octocat.github.io
#     # - git-consortium


#     #   2.  Enter a GitHub username: Novica-GH

#     # --- Top 5 latest pushed repositories for 'Novica-GH' ---
#     # - Lexicon_2026-27
#     # - Lexicon_1_Begining_ARCHIVED


#*******************************************************************************************
# LAB 1.3.4 Prove that the token is used
#---------------------------------------
# Look at the response headers. Print X-RateLimit-Limit with and without the token.
# With the token it should say 5000, without it 60. Hint: you need the whole response for
# this, so call requests.get directly.
#******************************************************************************************

# import os
# import requests
# from dotenv import load_dotenv

# # Load GITHUB_TOKEN from .env file
# load_dotenv()
# token = os.getenv("GITHUB_TOKEN")

# url = "https://api.github.com/users/octocat/repos"

# # --- 1. REQUEST WITHOUT TOKEN ---
# print("--- Request WITHOUT Token ---")
# response_no_auth = requests.get(url)
# limit_no_auth = response_no_auth.headers.get("X-RateLimit-Limit")
# print(f"Status Code: {response_no_auth.status_code}")
# print(f"X-RateLimit-Limit: {limit_no_auth}")

# print("\n" + "-" * 40 + "\n")

# # --- 2. REQUEST WITH TOKEN ---
# print("--- Request WITH Token ---")
# if not token:
#     print("Error: GITHUB_TOKEN not found in .env file.")
# else:
#     headers = {"Authorization": f"Bearer {token}"}
#     response_auth = requests.get(url, headers=headers)
#     limit_auth = response_auth.headers.get("X-RateLimit-Limit")
#     print(f"Status Code: {response_auth.status_code}")
#     print(f"X-RateLimit-Limit: {limit_auth}")


# Terminal:

    #     --- Request WITHOUT Token ---
    # Status Code: 200
    # X-RateLimit-Limit: 60

    # ----------------------------------------

    # --- Request WITH Token ---
    # Status Code: 200
    # X-RateLimit-Limit: 5000

#*******************************************************************************************
# LAB 1.3.5 Break the token on purpose
#-------------------------------------
# Change one character in your token and run the program again. Which status code do
# you get, and what does the message say? Expected: status 401 and a message about
# bad credentials. Is that 401 or 403, and what is the difference? Then fix the token again.
#******************************************************************************************

# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()
# token = os.getenv("GITHUB_TOKEN")

# if not token:
#     print("Error: GITHUB_TOKEN not found in .env file.")
#     exit(1)

# # Modifying one character in the token to break it:
# invalid_token = token[:-1] + ("0" if token[-1] != "0" else "1")

# url = "https://api.github.com/users/octocat/repos"
# headers = {"Authorization": f"Bearer {invalid_token}"}

# response = requests.get(url, headers=headers)

# print(f"Status Code: {response.status_code}")
# print("Response JSON:")
# print(response.json())


    # # Terminal: 
    # tatus Code: 401
    # Response JSON:
    # {'message': 'Bad credentials', 'documentation_url': 'https://docs.github.com/rest', 'status': '401'}



#*******************************************************************************************
# LAB 1.3.6 Check that the secret is safe
#----------------------------------------
# Run git init and then git status in your folder. The file .env must not appear in the
# list. If it does, your .gitignore is wrong. Fix it before you do anything else.g***************************************************************************************

# OK, done




# Terminal: 

#*******************************************************************************************
# LAB 1.3.7 Delete the token
#----------------------------
# When you are done, go back to the token page on GitHub and delete the token.
#******************************************************************************************

# Done - token deleted!




#############################################################################################
#********************************************************************************************
#  LAB 1.4  - Task/Lab 4: Bonus
#------------------------------
# 
# Real programs avoid asking an API the same thing again and again, for two reasons: rate limits,
# and speed. In this lab you add a simple cache to your weather tool. The program saves the
# answer in a file, and if the file is fresh enough, it reads from the file instead of calling the API.   
#                                                    *
#********************************************************************************************
# The idea
# if the file exists and is younger than 10 minutes:
# data = read the file
# else:
# data = call the API
# save data to the file
########################################################################


# Tasks:

#********************************************************************************************
#  LAB 1.4.1 Save the answer
#----------------------------
# After you get the weather, save the answer to a JSON file with json.dump. Run the
# program and open the file to see what is in it.
#******************************************************************************************


# import json
# from api_client import get_json

# GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
# FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
# CACHE_FILE = "weather_cache.json"


# def find_city(name: str) -> dict | None:
#     """Fetches coordinates for a given city name."""
#     url = f"{GEOCODING_URL}?name={name}&count=1"
#     data = get_json(url)

#     if not data or "results" not in data or not data["results"]:
#         return None

#     first_result = data["results"][0]
#     return {
#         "name": first_result.get("name"),
#         "country": first_result.get("country", ""),
#         "latitude": first_result.get("latitude"),
#         "longitude": first_result.get("longitude"),
#     }


# def fetch_and_cache_weather(lat: float, lon: float) -> dict | None:
#     """Fetches current weather from API and saves the raw response to a JSON file."""
#     url = f"{FORECAST_URL}?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
#     data = get_json(url)

#     if not data or "current" not in data:
#         return None

#     # Save the response dictionary directly to a local JSON file
#     with open(CACHE_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4)

#     print(f"\n[CACHE] Weather data saved successfully to '{CACHE_FILE}'.")
#     return data


# def main():
#     city_input = input("Enter a city name: ").strip()
#     if not city_input:
#         print("Please enter a valid city name.")
#         return

#     location = find_city(city_input)
#     if location is None:
#         print(f"Error: Could not find city '{city_input}'.")
#         return

#     # Fetch weather and write to JSON file
#     raw_weather = fetch_and_cache_weather(
#         location["latitude"], location["longitude"]
#     )
#     if raw_weather is None:
#         print("Error: Could not retrieve weather data.")
#         return

#     # Parse display values from response
#     current = raw_weather.get("current", {})
#     units = raw_weather.get("current_units", {})

#     temp = current.get("temperature_2m")
#     temp_unit = units.get("temperature_2m", "°C")
#     wind = current.get("wind_speed_10m")
#     wind_unit = units.get("wind_speed_10m", "km/h")

#     country_str = f", {location['country']}" if location["country"] else ""
#     print(
#         f"{location['name']}{country_str}: {temp}{temp_unit}, wind {wind} {wind_unit}"
#     )


# if __name__ == "__main__":
#     main()


# Terminal: 

    # Enter a city name: Stockholm

    # [CACHE] Weather data saved successfully to 'weather_cache.json'.
    # Stockholm, Sweden: 11.4°C, wind 21.2 km/h
    # - Komment - Everything is perfecto classico.... :)




#********************************************************************************************
#  LAB 1.4.2 Use the file when it is fresh
#-----------------------------------------
# Before you call the API, check if the file exists and is younger than 10 minutes. If it is,
# read the data from the file instead. Test it: run the program twice in a row, and make
# sure the second run does not call the API.
#******************************************************************************************

import json
import os
import time
from api_client import get_json

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
CACHE_FILE = "weather_cache.json"
CACHE_DURATION_SECONDS = 600  # 10 min


def find_city(name: str) -> dict | None:
    """Fetches coordinates for a given city name."""
    url = f"{GEOCODING_URL}?name={name}&count=1"
    data = get_json(url)

    if not data or "results" not in data or not data["results"]:
        return None

    first_result = data["results"][0]
    return {
        "name": first_result.get("name"),
        "country": first_result.get("country", ""),
        "latitude": first_result.get("latitude"),
        "longitude": first_result.get("longitude"),
    }


def get_weather(lat: float, lon: float) -> dict | None:
    """Returns weather data from local JSON cache if under 10 minutes old,

    otherwise fetches fresh data from Open-Meteo API.
    """
    # Check if cache file exists and is younger than 10 minutes
    if os.path.exists(CACHE_FILE):
        file_age = time.time() - os.path.getmtime(CACHE_FILE)
        if file_age < CACHE_DURATION_SECONDS:
            print(
                f"[CACHE HIT] Reading from '{CACHE_FILE}' (age: {int(file_age)}s)."
            )
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

    # If missing or expired -> API Call
    print("[API CALL] Cache missing or expired. Fetching fresh data...")
    url = f"{FORECAST_URL}?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
    data = get_json(url)

    if not data or "current" not in data:
        return None

    # Save fresh data to cache file
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return data


def main():
    city_input = input("Enter a city name: ").strip()
    if not city_input:
        print("Please enter a valid city name.")
        return

    location = find_city(city_input)
    if location is None:
        print(f"Error: Could not find city '{city_input}'.")
        return

    raw_weather = get_weather(location["latitude"], location["longitude"])
    if raw_weather is None:
        print("Error: Could not retrieve weather data.")
        return

    current = raw_weather.get("current", {})
    units = raw_weather.get("current_units", {})

    temp = current.get("temperature_2m")
    temp_unit = units.get("temperature_2m", "°C")
    wind = current.get("wind_speed_10m")
    wind_unit = units.get("wind_speed_10m", "km/h")

    country_str = f", {location['country']}" if location["country"] else ""
    print(
        f"{location['name']}{country_str}: {temp}{temp_unit}, wind {wind} {wind_unit}"
    )


if __name__ == "__main__":
    main()


# Terminal: 

    # Enter a city name: Stockholm
    # [CACHE HIT] Reading from 'weather_cache.json' (age: 29s).
    # Stockholm, Sweden: 11.4°C, wind 21.2 km/h



#********************************************************************************************
#  LAB 1.4.3 Explain why
#------------------------
# Write two sentences, as a comment in your code, about why this can be useful.


# Useful tools
# import json, os, time
# json.dump(data, file)
# json.load(file)
# os.path.exists(path)
# os.path.getmtime(path) # seconds since 1970
# time.time() # now, in the same unit

# Stuck? Read the error message from the bottom up, print the data you are working with, and then ask.
#****************************************************************************************************


#-------------------------- It is enough for today!!!
 






# Python & AI · Module 5 · API · Day 1 · Labs
# **********************************  END of LAB 1 API  ********************************************************